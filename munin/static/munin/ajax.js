var files={};
var json_files={};

function getXMLHttpRequest() {
	var xhr=null;
	if(window.ActiveXObject) {
		try {
			xhr=new ActiveXObject("Msxml2.XMLHTTP");
		} catch(e) {
			xhr=new ActiveXObject("Microsoft.XMLHTTP");
		}
	} else {
		xhr=new XMLHttpRequest();
	}
	return xhr;
}

function loadFile(file,callback) {
	var xhr=getXMLHttpRequest();
	xhr.onreadystatechange=function(){
		if(xhr.readyState==4 && (xhr.status==200||xhr.status==0)){
			files[file]=xhr.responseText;
			if(callback)
				callback();
		}
	}
	xhr.open("GET",file,true);
	xhr.send();
}

function loadJSON(file,callback) {
	function cb() {
		json_files[file]=JSON.parse(files[file]);
		if(callback)
			callback();
	}
	loadFile(file,cb);
}
