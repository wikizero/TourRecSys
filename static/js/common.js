$(function () {
    $("#nav li a").mouseenter(function () {
        $(this).css("background", "#008CD6")
<<<<<<< HEAD
    });

    $("#nav li a").mouseleave(function () {
        $(this).css("background", "#4C5A65")
    });

    $(".e_search_input").focus(function () {
        $(this).val("");
    });

    $(".e_search_input").blur(function () {
        var $this = $(this);
        if(!$this.val()){
            $this.val("搜索城市、国家、目的地…");
        }
    });

});
=======
    })

    $("#nav li a").mouseleave(function () {
        $(this).css("background", "#4C5A65")
    })
})
>>>>>>> cdd11c6ff9e43b14476997ed85ca3f324a331da7
