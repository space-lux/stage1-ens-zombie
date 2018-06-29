function sortHTML(els,f) {
	var e=[];
	var el=els.children;
	for(i in el) {
		e[i]=el[i];
	}
	e.sort(f);
	for(j in e) {
		if(e[j].clientWidth)//argh         Pour vérifier rapidement si on a affaire à un élément HTML et pas autre chose
			els.appendChild(e[j]);
	}
	return els;
}

function cloneNode(node) { // MERCI IE8
	var clone = node.nodeType == 3 ? document.createTextNode(node.nodeValue) : node.cloneNode(false);
	
	var child=node.firstChild;
	while(child) {
		clone.appendChild(cloneNode(child));
		child=child.nextSibling;
	}
	
	return clone;
}

function sign(x) {
	return x? x < 0 ? -1 : 1 : 0;
}
