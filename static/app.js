function preview() {
    var form = document.getElementById("form");
    form.aciton = "";
    form.submit();
}
    
function download() {
    var form = document.getElementById("form");
    form.action = "/markdown/download";
    form.submit();
}

function insert_word_pre(str) {
    var content = document.getElementById("content");
    if (document.selection) {
	var sel = document.selection.createRange();
	if (sel.text.length < 1) {
	    sel.text = str;
	} else {
	}
    } else {
	if (typeof content.selectionStart === 'number' && typeof content.selectionEnd === 'number') {
	    var startPos = content.selectionStart;
	    var endPos = content.selectionEnd;
	    if ((startPos == 0) || (content.value.charAt(startPos - 1) == '\n')) {
		content.value = content.value.substring(0, startPos) + str + content.value.substring(startPos, endPos) + content.value.substring(endPos, content.value.length+1);
		content.focus();
		content.selectionStart = endPos + str.length;
		content.selectionEnd = endPos + str.length;
		console.log(content.selectionEnd);
	    } else {
		content.value = content.value.substring(0, startPos) + '\n' + str + content.value.substring(startPos, endPos) + content.value.substring(endPos, content.value.length+1);
		content.focus();
		content.selectionStart = endPos + str.length + 1;
		content.selectionEnd = endPos + str.length + 1;
	    }
	} else {
	    content.value = str;
	    console.log(44444);
	}
    }
}

function insert_word_both(str) {
    var content = document.getElementById('content');
    if (document.selection) {
    } else {
	if (typeof content.selectionStart === 'number' && typeof content.selectionEnd === 'number') {
	    var startPos = content.selectionStart;
	    var endPos = content.selectionEnd;
	    content.value = content.value.substring(0, startPos) + str +content.value.substring(startPos, endPos) + str + content.value.substring(endPos, content.value.length+1);
	    content.focus();
	    if (endPos != startPos) {
		endPos += str.length;
	    }
	    content.selectionStart = endPos + str.length;
	    content.selectionEnd = endPos + str.length;
	}
    }
}

function insert_word_ol() { 
    var content = document.getElementById('content');
    if (document.selection) {
    } else {
	if (typeof content.selectionStart === 'number' && typeof content.selectionEnd === 'number') {
	    var startPos = content.selectionStart;
	    var endPos = content.selectionEnd;
	    if (startPos == 0) {
		insert_word_pre("1. ");
	    } else {
		var pos = content.value.substring(0,startPos-1).lastIndexOf("\n");
		if (pos == -1) {
		    pos = 0;
		}
		var tmpStr = content.value.substring(pos, startPos);
		var endp = tmpStr.indexOf('.');
		if (Number(tmpStr.substring(1, endp))) {
		    var count = "" + (Number(tmpStr.substring(1, endp)) + 1) + ". ";
		    insert_word_pre(count);
		} else {
		    insert_word_pre("\n1. ");
		}	
	    }
	}
    }
}

function insert_word_ul () {
    var content = document.getElementById('content');
    if (document.selection) {
    } else {
	if (typeof content.selectionStart === 'number' && typeof content.selectionEnd === 'number') {
	    var startPos = content.selectionStart;
	    var endPos = content.selectionEnd;
	    if (startPos == 0) {
		insert_word_pre("* ");
	    } else {
		var pos = content.value.substring(0,startPos-1).lastIndexOf("\n");
		if (content.value.charAt(pos+1) == '*') {
		    insert_word_pre("* ");
		} else {
		    insert_word_pre("\n* ");
		}
	    }
	}
    }
}
		
