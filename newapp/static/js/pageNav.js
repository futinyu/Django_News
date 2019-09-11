(function(){
    /**
     * 分页
     */
    var wrap = document.getElementById("pageNav")
    var prev = wrap.getElementsByClassName("page-prev")[0]
    var next = wrap.getElementsByClassName("page-next")[0]

    var oUl = wrap.getElementsByClassName("page-list")[0]
    var aLi = oUl.getElementsByTagName("li")
    
    var aLiWidth = 22
    var curPage = 0

    function calLeftDis() {
        for (var i=0; i<aLi.length; i++) {
            aLi[i].style.left = (-curPage*5 + i) * aLiWidth + "px"
        }
    }
    calLeftDis()

    prev.addEventListener("click", function(){
        if (curPage <= 0) return;
        curPage --;
        calLeftDis()
    })

    next.addEventListener("click", function(){
        if(curPage >= aLi.length/5 -1  ) return;
        curPage++
        calLeftDis()
    })
})()



// (function(){
//     /**
//      * 分页
//      */
//     var wrap = document.getElementById("pageNav")
//     var prev = wrap.getElementsByClassName("page-prev")[0]
//     var next = wrap.getElementsByClassName("page-next")[0]
//
//     var oUl = wrap.getElementsByClassName("page-list")[0]
//     var aLi = oUl.getElementsByTagName("li")
//
//     var aLiWidth = 22
//     var curPage = 0
//     function  calLeftDis() {
//         for(var i=0;i<aLi.length;i++)
//         {
//             ali[i].style.left=(-curPage*5+i)*aLiWidth+'px'
//         }
//     }
//     prev.addEventListener('click',function () {
//         if(curPage<=0)return;
//         curPage--
//         calLeftDis()
//     })
//     next.addEventListener('click',function () {
//         if(curPage>ali.length/5-1) return
//         curPage++
//         calLeftDis()
//     })
//     }()