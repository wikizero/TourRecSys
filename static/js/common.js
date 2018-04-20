$(function () {
    $("#nav li a").mouseenter(function () {
        $(this).css("background", "#008CD6")
    });

    $("#nav li a").mouseleave(function () {
        $(this).css("background", "#4C5A65")
    });

    $(".e_search_input").focus(function () {
        $(this).val("");
    });

    $(".e_search_input").blur(function () {
        var $this = $(this);
//        if(!$this.val()){
//            $this.val("搜索景点、城市…");
//        }
    });

    $(".city_name").mouseenter(function () {
        $(this).find("span").css("display", "none")
    });

    $(".city_name").mouseleave(function () {
        $(this).find("span").css("display", "block")
    });

});
