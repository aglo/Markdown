(function ($, undefined) {
    $.fn.getCursorPositionStart = function() {
	var el = $(this).get(0);
	var pos = 0;
	if ('selectionStart' in el) {
	    pos = el.selectionStart;
	} else if ('selection' in document) {
	    el.focus();
	    var Sel = document.selection.createRange();
	    var SelLength = document.selection.createRange().text.length;
	    Sel.moveStart('character', -el.value.length);
	    pos = Sel.text.length - SelLength;
	}
	return pos;
    }

    $.fn.getCursorPositionEnd = function() {
	var el = $(this).get(0);
	var pos = 0;
	if ('selectionEnd' in el) {
	    pos = el.selectionEnd;
	} else if ('selection' in document) {
	    el.focus();
	    var Sel = document.selection.createRange();
	    var SelLength = document.selection.createRange().text.length;
	    Sel.moveEnd('character', -el.value.length);
	    pos = Sel.text.length - SelLength;
	}
	return pos;
    }

    $.fn.setCursorPosition = function(start, end) {
	return this.each(function() {
	    if (this.setSelectionRange) {
		this.focus();
		this.setSelectionRange(start, end);
	    } else if (this.createTextRange) {
		var range = this.createTextRange();
		range.collapse(true);
		range.moveEnd('character', end);
		range.moveStart('character', start);
		range.select();
	    }
	});
    };
})(jQuery);

function preview() {
    var form = $("#form");
    form.attr('action', '/markdown');
    form.submit();
}

function download() {
    var form = $("#form");
    form.attr('action', '/markdown/download');
    form.submit();
}

function insert_word_pre(str) {

    var insertstr = "";
    switch(str) {
    case "head1":
	insertstr = "# ";
	break;
    case "head2":
	insertstr = "## ";
	break;
    case "head3":
	insertstr = "### ";
	break;
    case "bq":
	insertstr = "> ";
	break;
    case "hr":
	insertstr = "***\n";
	break;
    default:
	insertstr = str;
	break;
    }

    var tmpStr = $("#content").val();
    var startPos = $("#content").getCursorPositionStart();
    var endPos = $("#content").getCursorPositionEnd();

    if ((startPos == 0) || (tmpStr.charAt(startPos-1) == '\n')) {
	tmpStr = tmpStr.substring(0, startPos)
	    + insertstr
	    + tmpStr.substring(startPos, endPos)
	    + tmpStr.substring(endPos, tmpStr.length+1);
	startPos = endPos + insertstr.length;
	endPos = endPos + insertstr.length;
    } else {
	tmpStr = tmpStr.substring(0, startPos)
	    + '\n'
	    + insertstr
            + tmpStr.substring(startPos, endPos)
            + tmpStr.substring(endPos, tmpStr.length+1);
	startPos = endPos + insertstr.length + 1;
	endPos = endPos + insertstr.length + 1;
    }
    $("#content").val(tmpStr);
    $("#content").setCursorPosition(startPos, endPos);
}

function insert_word_both(str) {

    var insertstr = "";
    switch(str) {
    case "bold":
	insertstr = "**";
	break;
    case "italic":
	insertstr = "_";
	break;
    case "code":
	insertstr = "`";
	break;
    default:
	break;
    }

    var content = $("#content");
    var tmpStr = $("#content").val();
    var startPos = $("#content").getCursorPositionStart();
    var endPos = $("#content").getCursorPositionEnd();

    tmpStr = tmpStr.substring(0, startPos)
        + insertstr
        + tmpStr.substring(startPos, endPos)
        + insertstr
	+ tmpStr.substring(endPos, tmpStr.length+1);

    if (endPos != startPos) {
	endPos += insertstr.length;
    }
    endPos += insertstr.length;
    $("#content").val(tmpStr);
    $("#content").setCursorPosition(endPos, endPos);
}

function insert_word_ol() {

    var startPos = $("#content").getCursorPositionStart();
    var endPos = $("#content").getCursorPositionEnd();

    if (startPos == 0) {
	insert_word_pre("1. ");
    } else {
	var pos = $("#content").val().substring(0,startPos-1).lastIndexOf("\n");
	if (pos == -1) {
	    pos = 0;
	}
	var tmpStr = $("#content").val().substring(pos, startPos);
	var endp = tmpStr.indexOf('.');
	if (Number(tmpStr.substring(1, endp))) {
	    var count = "" + (Number(tmpStr.substring(1, endp))+1) + ". ";
	    insert_word_pre(count);
	} else {
	    insert_word_pre("\n1. ");
	}
    }
}

function insert_word_ul() {

    var content = $("#content");
    var startPos = $("#content").getCursorPositionStart();
    var endPos = $("#content").getCursorPositionEnd();

    if (startPos == 0) {
	insert_word_pre("* ");
    } else {
	var pos = $("#content").val().substring(0,startPos-1).lastIndexOf("\n");
	if ($("#content").val().charAt(pos+1) == '*') {
	    insert_word_pre("* ");
	} else {
	    insert_word_pre("\n* ");
	}
    }
}

function insert_link(str) {

    var text = "#" + str + "text";
    var url = "#" + str + "url";
    var linktext = $(text).val();
    var linkurl = $(url).val();

    if (linktext == "") {
	var alertstr = "please input " + str +" text";
	alert(alertstr);
	return;
    }
    if (linkurl =="") {
	var alertstr = "please input " + str + " url"
	alert(alertstr);
	return;
    }

    var content = $("#content");
    var startPos = $("#content").getCursorPositionStart();
    var endPos = $("#content").getCursorPositionEnd();
    var tmp = ""
    var tmpStr = $("#content").val()

    if (str == "link") {
	tmp = "["
    }
    if (str == "image") {
	tmp = "!["
    }

    tmpStr = tmpStr.substring(0,startPos)
	+ tmp
	+ linktext
	+ "]("
	+ linkurl
	+ ")"
	+ tmpStr.substring(endPos, tmpStr.length+1);

    $("#content").val(tmpStr);
    $("button.datadis").attr("data-dismiss", "modal");
}

$("#Pic-cli").on("click", function() {
    var startPos = $("#content").getCursorPositionStart();
    var endPos = $("#content").getCursorPositionEnd();
    if (startPos == endPos) {
	$("#imagetext").val("");
    } else {
	$("#imagetext").val($("#content").val().substring(startPos, endPos));
    }
    $("#imageurl").val("");
});

$("#Lin-cli").on("click", function() {
    var startPos = $("#content").getCursorPositionStart();
    var endPos = $("#content").getCursorPositionEnd();
    if (startPos == endPos) {
	$("#linktext").val("");
    } else {
	$("#linktext").val($("#content").val().substring(startPos, endPos));
    }
    $("#linkurl").val("");
});