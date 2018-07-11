// ViCompte dépend de DraC
var ViCompte=(function(){
	var self={};
	// d={min:0,max:11,value:caca};
	self.speedCounter=function(c,d,t) {
		var	w=c.width,
			h=c.height,
			fontsize=15,
			s=Math.min(h/2,w/2),
			circle_s=0.7,
			pointer_s=0.2,
			angle=0.7*2*Math.PI,
			line_width=5,
			angle_start=Math.PI*1.5-angle*0.5,
			angle_end=(angle-Math.PI)*0.5;
			
		c=c.getContext("2d");
		c.clearRect(0,0,w,h);
		var grd=c.createLinearGradient(w/2-s,0,w/2+s,0);
		grd.addColorStop(0,'blue');
		grd.addColorStop(1,'red');
		
		c.beginPath();
		c.arc(w/2,h/2,s*(1+circle_s)/2,angle_start,angle_end);
		c.strokeStyle=grd;
		c.lineWidth=s*(1-circle_s);
		c.stroke();
		
		
		var pointer_angle=angle_start*1+(Math.PI*2+angle_end-angle_start)*d.value/(d.max-d.min);
		
		c.beginPath();
		c.moveTo(w/2+s*pointer_s*Math.cos(pointer_angle-Math.PI/2),h/2+s*pointer_s*Math.sin(pointer_angle-Math.PI/2));
		c.lineTo(w/2+s*(1+circle_s)*0.5*Math.cos(pointer_angle),h/2+s*(1+circle_s)*0.5*Math.sin(pointer_angle));
		c.lineTo(w/2+s*pointer_s*Math.cos(pointer_angle+Math.PI/2),h/2+s*pointer_s*Math.sin(pointer_angle+Math.PI/2));
		c.lineWidth=2;
		c.fillStyle="white";
		c.strokeStyle="gray";
		c.fill();
		c.stroke();
		
		c.beginPath();
		c.arc(w/2,h/2,s*pointer_s,0,2*Math.PI);
		c.fillStyle="black";
		c.fill();
		
		if(t) {
			c.font=fontsize+"px Arial";
			c.textAlign="center";
			c.textBaseline="top";
			c.fillText(t,w/2,h/2+s*pointer_s*1.5);
		}
	};
	
	return self;
})();
