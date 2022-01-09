
// ready() can run the functions below after the html page has been loaded
$(document).ready(function () {


    //the click() for the "show_button" classes

    $(".show_button").on('click', function () {

        //$(this).means the DOM object which is clicked

        // next() is used to find the next element of this DOM object, data() is used to retrieve the data-status
        let status = $(this).next(".hidden_text").data("status");

        let div_block = $(this).next(".hidden_text");

        if (status == "hidden") {
            $(this).next(".hidden_text").data("status", "show");

            //show() can change style = "display:none" to style = "display: block"
            div_block.show();
        } else {
            $(this).siblings(".hidden_text").data("status", "hidden");

            //show() can change style = "display:block" to style = "display: none"
            div_block.hide();
        }
    });


    $(".think_aloud").on('click', function () {

        //siblings is used to find the siblings of the current DOM object
        let text_obj = $(this).siblings(".selection_box").children(".think_aloud_txt");
        let status = text_obj.data("status");


        if (status == "hidden") {
            text_obj.data("status", "show");
            $(this).siblings(".selection_box").children(".source_txt").data("status", "hidden");
            $(this).siblings(".selection_box").children(".source_txt").hide();
            $(this).siblings(".selection_box").children(".lab_study_txt").data("status", "hidden");
            $(this).siblings(".selection_box").children(".lab_study_txt").hide();
            text_obj.show();
        }

    });

    $(".crowed_source").on('click', function () {


        let text_obj = $(this).siblings(".selection_box").children(".source_txt");
        let status = text_obj.data("status");


        if (status == "hidden") {
            text_obj.data("status", "show");
            $(this).siblings(".selection_box").children(".think_aloud_txt").data("status", "hidden");
            $(this).siblings(".selection_box").children(".think_aloud_txt").hide();
            $(this).siblings(".selection_box").children(".lab_study_txt").data("status", "hidden");
            $(this).siblings(".selection_box").children(".lab_study_txt").hide();
            text_obj.show();
        }

    });

    $(".lab_study").on('click', function () {

        let text_obj = $(this).siblings(".selection_box").children(".lab_study_txt");
        let status = text_obj.data("status");


        if (status == "hidden") {

            text_obj.data("status", "show");
            $(this).siblings(".selection_box").children(".source_txt").data("status", "hidden");
            $(this).siblings(".selection_box").children(".source_txt").hide();
            $(this).siblings(".selection_box").children(".think_aloud_txt").data("status", "hidden");
            $(this).siblings(".selection_box").children(".think_aloud_txt").hide();
            text_obj.show();
        }

    });

    $(".think_aloud_p").on('click', function () {

        //parents() : find its ancesstors  children: find its children

        let text_area = $(this).parents(".inspect").children("textarea");


        //text() get html text of that DOM object
        let text = $(this).text();

        //val() get the value of the attribute 

        text_area.val(text);

    });

    $(".source_txt_p").on('click', function () {

        let text_area = $(this).parents(".inspect").children("textarea");

        let text = $(this).text();

        text_area.val(text);

    });

    $(".lab_study_p").on('click', function () {

        let text_area = $(this).parents(".inspect").children("textarea");

        let text = $(this).text();

        text_area.val(text);

    });

});





