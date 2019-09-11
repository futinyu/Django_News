(function(){
    var input = document.getElementById("comments-input");//输入框
    var btn = document.getElementById("input-submit");//提交
    var oUl = document.getElementById("comments-list");
    var comments = [];

    // ajax
    /**
     * 获取评论列表
     * */
    function  getCommentsList() {
        // console.log(newId)
        $.ajax({
            method:"GET",
            url:"/new/ajax_get_comment",
            success: function (res) {
                var jsonObj = JSON.parse(res)

                if(jsonObj.status){
                    var data = jsonObj.data
                    comments = data;
                    // console.log(data)
                    oUl.innerHTML = ""
                    var arr = document.cookie.split(";");
                    var isAdmin;
                    for (var i=0; i<arr.length; i++){
                        var key = arr[i].split("=")[0]
                        console.log(key)
                        if (key === " isadmin"){
                            isAdmin = arr[i].split("=")[1]
                        }
                    }
                    console.log(isAdmin)
                    for(var i=0; i< data.length; i++){
                        var date = calTimeDis(data[i].commentDate)
                        var template = `
                                <div class="list-header">
                                    <span class="header-title">${data[i].nameID__userName}</span>
                                    <span class="header-puttime">${date}</span>
                                    <span class="header-close"><img class="icon-16 comment-close" src="/static/img/close.png" alt="close"></span>     
                                </div>
                                 <div class="list-main">${data[i].commentContent}</div>
                                 <div class="like-box"><img  class="icon-18 toLike" src="/static/img/like.png" alt="like">${data[i].commentFavorite}</div>
                            `
                        var aLi = document.createElement("li")
                        aLi.innerHTML = template
                        oUl.append(aLi)
                    }

                    $(".comment-close").each(function (index, item) {
                        if(!Number(isAdmin)) {
                            // 不是管理员
                            item.style.display = "none"
                            return
                        }
                        item.onclick = function () {
                            commentId = comments[index].commentID
                            $.ajax({
                                method: "GET",
                                url: "/new/ajax_del_comment",
                                data:{
                                    commentid: commentId
                                },
                                success: function (res) {
                                    var res = JSON.parse(res)
                                    if(res.status){
                                        getCommentsList()
                                    }else{
                                        alert("你怕是个魔教中人")
                                    }
                                }
                            })
                        }
                    })

                    $(".toLike").each(function (index, item) {
                        item.onclick = function () {
                            commentId = comments[index].commentID
                            $.ajax({
                                method: "GET",
                                url: "/new/ajax_favorite",
                                data:{
                                    commentid: commentId
                                },
                                success: function (res) {
                                    var res = JSON.parse(res)
                                    if(res.status){
                                        getCommentsList()
                                    }else{
                                        alert("你怕是个魔教中人")
                                    }
                                }
                            })
                        }
                    })
                }
                else{
                    alert("你怕是个魔教中人")
                }
            }
        })
    }
    /**
     * 计算时间差
     * @param timestap
     * @return string
     * */
    function calTimeDis(timestap){
        var date = new Date(timestap)
        var now = Date.now()/1000  //转成unix时间戳
        var dis = now - date;
        if (dis < 60 * 60) {
            return "刚刚"
        }else if (dis < 24 * 60 * 60) {
            return "一小时前"
        }else if (dis < 30 * 24 * 60 * 60) {
            return "一天前"
        }else if (dis < 365 * 24 * 60 * 60){
            return "一个月前"
        }else{
            return "一年前"
        }

    }

    getCommentsList()

    btn.onclick = function () {
        var inputText = input.value.trim()
        if(inputText == "") return
        else{
            $.ajax({
                url:"/new/ajax_add_comment",
                method:"POST",
                headers:{"X-CSRFToken":document.cookie.split(";")[0].split("=")[1]},
                data:{
                    context:inputText
                },
                success:function (res) {
                    var res = JSON.parse(res)
                    if (res.status) {
                        input.value = "";
                        getCommentsList()
                    }else{
                        alert("你怕是个魔教中人!快去登录")
                    }
                }
            })
        }
    }


})()