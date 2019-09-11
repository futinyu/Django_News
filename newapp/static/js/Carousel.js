// 从第二张图片开始轮播
var Carousel = (function (){
	var timer = null;//私有变量
	var Default = { //默认参数
		timing:'linear',
		duration:'1s',
		transferTime:3000,
		type:'Horizontal'
	};
	function Carousel(option){
		this.oUl = option.oUl;
		this.transferTime = option.transferTime ? option.transferTime:Default.transferTime;
		this.container = this.oUl.parentNode;
		this.aLi = this.oUl.children;
		this.timing = option.timing ? option.timing:Default.timing;
		this.duration = parseInt(option.duration) > 1 ?	Default.duration:option.duration;
		this.liLength = this.aLi.length;
		switch(option.type? option.type:Default.type){
			case 'Horizontal':
				this.type = 'left';
				this.changeNum = this.aLi[0].offsetWidth;
				break;
			case 'Vertical':
				this.type = 'bottom';
				this.changeNum = this.aLi[0].offsetHeight;
				break;
			default:
				break;
		}
		this.init();
		this.start();
		this.bindEvent();
	}

	Carousel.prototype = {
		init(){
			this.oUl.style.overflow = 'hidden';
			this.oUl.style.position = 'relative';
			[].forEach.call(this.aLi,(item,index)=>{	
				item.style[this.type] = (index-1) * this.changeNum + 'px';
			});
			this.addPicTitle();
			this.addCtrl();
			this.addDot();
		},
		addCtrl(){
			//添加按钮
			this.prevBtn = document.createElement('div');
			this.nextBtn = document.createElement('div');
			this.prevBtn.className = "poster-btn poster-prev-btn";
			this.nextBtn.className = "poster-btn poster-next-btn";
			this.container.appendChild(this.prevBtn);
			this.container.appendChild(this.nextBtn);
		},
		addDot(){
			//添加小点
			this.dot = document.createElement('div');
			this.dot.className = "dot";
			this.dot.innerHTML = "<ul></ul>";
			this.container.appendChild(this.dot);
			this.dotUl = this.dot.children;
			for(let i=0;i<this.liLength;i++){
				this.dotUl[0].appendChild(document.createElement('li'));	
			}
			this.dotUl[0].firstChild.nextSibling.className="dotHover";
			this.dotLi = this.dotUl[0].children;
			for(let i=0;i<this.liLength;i++){
				this.dotLi[i].key = i;
			}
			this.clientImg = 1;
	
			this.addClickEvent();
		},
		addClickEvent(oUl){
			this.dotUl[0].addEventListener('click',(e)=>{
				//console.log(e.target.key,this.clientImg)
				var clientPic = this.clientImg;
				if(e.target.key > clientPic){
					for(let i=0;i<(e.target.key-clientPic);i++){
						this.next();
					}
					this.clientImg = e.target.key;
				}else{
					for(let i=0;i<(clientPic-e.target.key);i++){
						this.prev();
					}
					this.clientImg = e.target.key;
				}
			})
		},
		addPicTitle(){
			//添加图片标题
			var aLiDom = document.querySelectorAll('.'+this.aLi[0].className+' a');
			for(let i=0;i<this.liLength;i++){
				var title = document.createElement('h4');
				title.className = 'pic_title';
				title.innerText = aLiDom[i].firstChild.alt 
				aLiDom[i].appendChild(title);
			}	
		},
		dotRun(){
			[].forEach.call(this.aLi,(item,index)=>{
				this.dotLi[index].className = "";
				if(parseInt(item.style[this.type]) == 0){
					this.dotLi[index].className = "dotHover";
					this.clientImg = index;
				}
			})
		},
		next(){
			[].forEach.call(this.aLi,(item)=>{
				if(parseInt(item.style[this.type]) <= -this.changeNum){
					item.style.transition = `${this.type} 0s ${this.timing}`;
					item.style[this.type] = this.changeNum * (this.liLength - 2) + 'px';
				}
				else{
					item.style.transition = `${this.type} ${this.duration} ${this.timing}`;
					item.style[this.type] = parseInt(item.style[this.type]) - this.changeNum + 'px';
				}
				this.dotRun();
			});
		},
		prev(){
			[].forEach.call(this.aLi,(item)=>{
				if(parseInt(item.style[this.type]) >= this.changeNum * (this.liLength - 2)){
					item.style.transition = `${this.type} 0s ${this.timing}`;
					item.style[this.type] =  - this.changeNum + 'px';
				}
				else{
					item.style.transition = `${this.type} ${this.duration} ${this.timing}`;
					item.style[this.type] = parseInt(item.style[this.type]) + this.changeNum + 'px';
				}
				this.dotRun();
			});
		},
		start(){
			timer = setInterval(this.next.bind(this), this.transferTime);
		},
		stop(){
			clearInterval(timer);
		},
		bindEvent(){
			this.container.onmouseenter = this.stop.bind(this);
			this.container.onmouseleave = this.start.bind(this);
			this.prevBtn.onclick = this.prev.bind(this);
			this.nextBtn.onclick = this.next.bind(this);
		}
	};
	return Carousel;
}())
// ES6
// class Carousel{
// 	constructor(option){
// 		this.oUl = option.oUl;
// 		this.container = this.oUl.parentNode;
// 		this.aLi = this.oUl.children;
// 		this.timing = option.timing ? option.timing:"linear";
// 		this.duration = parseInt(option.duration) > 1?'1s':option.duration;
// 		this.liLength = this.aLi.length;
// 		timer = null;
// 		switch(option.type? option.type:'Horizontal'){
// 			case 'Horizontal':
// 				this.type = 'left';
// 				this.changeNum = this.aLi[0].offsetWidth;
// 				break;
// 			case 'Vertical':
// 				this.type = 'bottom';
// 				this.changeNum = this.aLi[0].offsetHeight;
// 				break;
// 			default:
// 				break;
// 		}
// 		this.init();
// 		this.start();
// 		this.bindEvent();
// 	};
// 	init(){
// 		this.oUl.style.overflow = 'hidden';
// 		this.oUl.style.position = 'relative';
// 		[].forEach.call(this.aLi,(item,index)=>{	
// 			item.style[this.type] = (index-1) * this.changeNum + 'px';
// 		});
// 		this.addPicTitle();
// 		this.addCtrl();
// 		this.addDot();
// 	};
// 	addCtrl(){
// 		//添加按钮
// 		this.prevBtn = document.createElement('div');
// 		this.nextBtn = document.createElement('div');
// 		this.prevBtn.className = "poster-btn poster-prev-btn";
// 		this.nextBtn.className = "poster-btn poster-next-btn";
// 		this.container.appendChild(this.prevBtn);
// 		this.container.appendChild(this.nextBtn);
// 	};
// 	addDot(){
// 		//添加小点
// 		this.dot = document.createElement('div');
// 		this.dot.className = "dot";
// 		this.dot.innerHTML = "<ul></ul>";
// 		this.container.appendChild(this.dot);
// 		this.dotUl = this.dot.children;
// 		for(let i=0;i<this.liLength;i++){
// 			this.dotUl[0].appendChild(document.createElement('li'));	
// 		}
// 		this.dotUl[0].firstChild.nextSibling.className="dotHover";
// 		this.dotLi = this.dotUl[0].children;
// 		for(let i=0;i<this.liLength;i++){
// 			this.dotLi[i].key = i;
// 		}
// 		this.clientImg = 1;

// 		this.addClickEvent(this.dotUl[0]);
// 	};
// 	addClickEvent(oUl){
// 		oUl.addEventListener('click',(e)=>{
// 			//console.log(e.target.key,this.clientImg)
// 			var clientPic = this.clientImg;
// 			if(e.target.key > clientPic){
// 				for(let i=0;i<(e.target.key-clientPic);i++){
// 					this.next();
// 				}
// 				this.clientImg = e.target.key;
// 			}else{
// 				for(let i=0;i<(clientPic-e.target.key);i++){
// 					this.prev();
// 				}
// 				this.clientImg = e.target.key;
// 			}
// 		})
// 	};
// 	addPicTitle(){
// 		//添加图片标题
// 		var aLiDom = document.querySelectorAll('.'+this.aLi[0].className+' a');
// 		for(let i=0;i<this.liLength;i++){
// 			var title = document.createElement('h4');
// 			title.innerText = aLiDom[i].firstChild.alt 
// 			aLiDom[i].appendChild(title);
// 		}	
// 	};
// 	dotRun(){
// 		[].forEach.call(this.aLi,(item,index)=>{
// 			this.dotLi[index].className = "";
// 			if(parseInt(item.style[this.type]) == 0){
// 				this.dotLi[index].className = "dotHover";
// 				this.clientImg = index;
// 			}
// 		})
// 	};
// 	next(){
// 		[].forEach.call(this.aLi,(item)=>{
// 			if(parseInt(item.style[this.type]) <= -this.changeNum){
// 				item.style.transition = `${this.type} 0s ${this.timing}`;
// 				item.style[this.type] = this.changeNum * (this.liLength - 2) + 'px';
// 			}
// 			else{
// 				item.style.transition = `${this.type} ${this.duration} ${this.timing}`;
// 				item.style[this.type] = parseInt(item.style[this.type]) - this.changeNum + 'px';
// 			}
// 			this.dotRun();
// 		});
// 	};
// 	prev(){
// 		[].forEach.call(this.aLi,(item)=>{
// 			if(parseInt(item.style[this.type]) >= this.changeNum * (this.liLength - 2)){
// 				item.style.transition = `${this.type} 0s ${this.timing}`;
// 				item.style[this.type] =  - this.changeNum + 'px';
// 			}
// 			else{
// 				item.style.transition = `${this.type} ${this.duration} ${this.timing}`;
// 				item.style[this.type] = parseInt(item.style[this.type]) + this.changeNum + 'px';
// 			}
// 			this.dotRun();
// 		});
// 	};
// 	start(){
// 		timer = setInterval(this.next.bind(this),3000);
// 	};
// 	stop(){
// 		clearInterval(timer);
// 	};
// 	bindEvent(){
// 		this.container.onmouseenter = this.stop.bind(this);
// 		this.container.onmouseleave = this.start.bind(this);
// 		this.prevBtn.onclick = this.prev.bind(this);
// 		this.nextBtn.onclick = this.next.bind(this);
// 	}
// }