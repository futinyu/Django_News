function fun0(){
	var yhm=document.getElementById('yhm').value.trim();//移除字符串两侧的空白字符
	var user=document.getElementById('user').value.trim();
	var pwd=document.getElementById('pwd').value.trim();
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



function fun4(){
	var d = document.getElementById("user") .value;
	//alert(d)
	var e = /^1[3578]\d{0,9}|\w{5,}@(qq.com|163.com)$/;
	var f = e.test(d);
	//alert(f)
	if(f){
		document.getElementsByClassName("username")[0].innerHTML="";

	}else{
		document.getElementsByClassName("username")[0].innerHTML="ERROR:输入有误！";
		document.getElementsByClassName("username")[0].style.color="red";
	}

}