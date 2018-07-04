// Voluspa dépend de DraC
var Voluspa=(function(){
	var self={};
	
	self.roundTable=function(c,d,u){
		var	w=c.width,
			h=c.height,
			mini=0,
			maxi=0,
			n=d.length,
			fontsize=15,
			s=Math.min(h/2,w/2),
			circles_s=0.7,
			angle_step=Math.PI*2/n,
			values=[],
			wmin=5,
			wmax=20,
			ccs=wmax*1.5,
			colors=DraC.createColorSet(d.length);
		c=c.getContext("2d");
		c.clearRect(0,0,w,h);
		c.font=fontsize+"px Arial";
		c.textAlign="center";
		wmax=Math.min(wmax,wmax*9/n);
		s-=wmax;
		circles_s*=2*s/(n);
		circles_s=Math.min(circles_s,s/2-ccs);
		s-=circles_s;
		for(var i=0;i<d.length;i++) {
			colors[i]='rgb('+colors[i].r+','+colors[i].g+','+colors[i].b+')';
			if(d[i].color)
				colors[i]=d[i].color;
			values[i]=Math.abs(d[i].value);
		}
		mini=DraC.min(values);
		maxi=DraC.max(values);
		for(var i=0;i<d.length;i++) {
			c.beginPath();
			c.fillStyle=colors[i];
			c.lineWidth=wmin+(wmax-wmin)*(values[i]-mini)/(maxi-mini);
			c.strokeStyle=d[i].value<0?"black":"white";
			var	x=w/2+s*Math.sin(i*angle_step),
				y=h/2+s*Math.cos(i*angle_step);
			c.arc(x,y,circles_s+c.lineWidth/2,0,2*Math.PI);
			c.fill();
			if(d[i].value)
				c.stroke();
			c.strokeStyle=colors[i];
			c.beginPath();
			c.moveTo(x,y);
			c.lineTo(w/2,h/2);
			c.stroke();
			c.fillStyle="black";
			c.lineWidth=2;
			c.strokeText(d[i].label,x,y);
			c.strokeText(d[i].value,x,y+fontsize);
			c.fillText(d[i].label,x,y);
			c.fillText(d[i].value,x,y+fontsize);
		}
		c.fillStyle="#aaa";
		c.beginPath();
		c.arc(w/2,h/2,ccs,0,2*Math.PI);
		c.fill();
		if(d.center) {
			c.fillStyle="black";
			c.textBaseline="middle";
			for(var i in d.center) {
				if(d.center[i])
					c.fillText(d.center[i],w/2,(i*1+0.5-d.center.length/2)*fontsize+h/2);
			}
		}
	}
	
	return self;
})();
