function fun0(){
	
	var user=document.getElementById('yhm').value.trim()
	var user=document.getElementById('user').value.trim()
	var pwd=document.getElementById('pwd').value.trim()
	if(user.length==0||pwd.length==0||yhm.length==0){
		alert('表单数据不能为空')
		//document.getElementsByClassName("yhm")[0].innerText="*";
		//document.getElementsByClassName("username")[0].innerText="*";
		//document.getElementsByClassName("password")[0].innerText="*";
		//document.getElementsByClassName("yhm").style.color="red";
		//document.getElementsByClassName("username").style.color="red";
		//document.getElementsByClassName("password").style.color="red";
	}
}
function fun2(){
	var d = document.getElementById("user") .value;
	//alert(d)
	var e = /^1[3578]\d{0,9}|\w{5,}@(qq.com|163.com)$/;
	var f = e.test(d);
	//alert(f)
	if(f){
		document.getElementsByClassName("username")[0].innerHTML="";
		
	}else{
		document.getElementsByClassName("username")[0].innerHTML="ERROR";
		document.getElementsByClassName("username")[0].style.color="red";
	}
	
}
function fun3(){
	var password = document.getElementById("pwd").value;
				
		if(password.length>16)
			{alert('密码过长，请重新输入！')}
		else{
			var a1=0;
			var b1=0;
			var c1=0;
			if(password.length !=0){
				for(i=0;i<password.length;i++){
					var p=password[i];
					var l=p.charCodeAt();
						if(l>=48&&l<=57)
							{a1=1;}
						if(l>=65&&l<=90)
							{b1=1;}
						if(l>=97&&l<=122)
							{c1=1;}
						var m=a1+b1+c1;
						if (m==1){
							document.getElementById("r").style.backgroundColor="red";
							document.getElementById("z").style.backgroundColor="white";
							document.getElementById("q").style.backgroundColor="white";
							}
						else if (m==2){
							document.getElementById("r").style.backgroundColor="orange";
							document.getElementById("z").style.backgroundColor="orange";
							document.getElementById("q").style.backgroundColor="white";
							}
						else if (m==3){
							document.getElementById("r").style.backgroundColor="green";
							document.getElementById("z").style.backgroundColor="green";
							document.getElementById("q").style.backgroundColor="green";
							}
					
			
				}
			}
				else{
					document.getElementById("r").style.backgroundColor="white";
					document.getElementById("z").style.backgroundColor="white";
					document.getElementById("q").style.backgroundColor="white";
				}
			
		}
}
