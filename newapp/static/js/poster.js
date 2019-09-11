$(document).ready(function () {//读取完页面所有的HTML代码再读取以下JS/jq代码
    //alert(i);
    var i = 0;

    var clone = $(".banner .img li").first().clone();//克隆第一张图片
    $(".banner .img").append(clone);//复制到列表最后
    var size = $(".banner .img li").size();//拿到属性一致的图片个数
   

    for (var j = 0; j < size-1; j++) {  //循环出4个圆点点击的图片
        $(".banner .num").append("<li></li>");
    }

    $(".banner .num li").first().addClass("on"); //拿到第一条给他一个class 也就是背景颜色

    /*自动轮播*/

    var t = setInterval(function () { //2秒钟循环的执行move这个方法
        i++; 
        move();
    },3000);

    /*鼠标悬停事件*/

    $(".banner").hover(function () {
        clearInterval(t);//鼠标悬停时清除定时器
    }, function () {
        t = setInterval(function () { i++; move(); }, 3000); //鼠标移出时继续执行定时器
    });




    /*鼠标滑入圆点事件*/

    $(".banner .num li").hover(function () {

        var index = $(this).index();//获取当前索引值
        i = index;
        $(".banner .img").stop().animate({ left: -index * 1440 }, 500);
        $(this).addClass("on").siblings().removeClass("on");
    });



    /*向左按钮*/
    $(".banner .btn_l").click(function () {
        i--;
        move();
    })

    
    /*向右按钮*/
    $(".banner .btn_r").click(function () {
        i++;
        move();
    })

    /*移动事件*/
    function move() {
        //alert(i);
        //alert(size);
        if (i == size) {
            $(".banner .img").css({ left: 0});
            i = 1;
        }
        if (i == -1) {
            $(".banner .img").css({ left: -(size - 1) * 1440});//转动1个图片宽
            i = size - 2;
        }
        $(".banner .img").stop().animate({ left: -i * 1440 }, 500);

        if (i == size - 1) {
            $(".banner .num li").eq(0).addClass("on").siblings().removeClass("on");

        } else {
            $(".banner .num li").eq(i).addClass("on").siblings().removeClass("on");
            
        }
        
    }
});
	/*下轮播*/
	 xia=setInterval(fu,2000);
function fu(){
	$(".zizhi_2_1_1").animate({
	marginLeft:'-269px'},500,
	function(){
  $(".zizhi_2_1_1").css("margin-left","0px"),
  $(".zizhi_2_1_1").append($(".zizhi_2_1_1 img:first"))
})}
 $(function(){
  $(".zuo").click(function(){
	$(".zizhi_2_1_1").animate({
	marginLeft:'-269px'},500,
	function(){
		$(".zizhi_2_1_1").css("margin-left","0px"),
		$(".zizhi_2_1_1").append($(".zizhi_2_1_1 img:first"))
	}
	)});
  $(".you").click(function(){
	$(".zizhi_2_1_1").animate({
	marginLeft:'269px',
  },500,
  function(){
		$(".zizhi_2_1_1").css("margin-left","0px"),
		$(".zizhi_2_1_1").prepend($(".zizhi_2_1_1 img:last"))
	}
  )})
})
 $('.zuo,.you,.zizhi_2').hover(function(){
	clearInterval(xia)
 },function(){
  xia=setInterval(fu,2000);
 })