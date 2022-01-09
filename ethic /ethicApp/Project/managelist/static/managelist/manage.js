function convert_date(dates){

    let arr = dates.split("/");

    let total = ""
    total = total.concat(arr[2], arr[1], arr[0]);

    return date_num = Number(total);
}


$('document').ready(function(){

    $('#search').keyup(function(e){
      
      let value = $(this).val().toLowerCase();

      $(".row").filter(function() {

        $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
      
    });

    $(".threedots").siblings(".links").hide();


});

function deactivateAll(current){
    $( ".threedots" ).each(function( index, elem ){
        if (elem != current && $(elem).hasClass("active")) {
            $(elem).siblings(".links").slideUp("fast");
            $(elem).removeClass("active");
        }
    });
}


$(document).on("click", function(event){
    var $trigger = $(".threedots");
    if($trigger !== event.target && !$trigger.has(event.target).length){
        $(".links").slideUp("fast");
    } 
    
});

$(document).on("click", ".threedots", function(){
    deactivateAll(this);
    $(this).siblings(".links").slideToggle("fast");
    $(this).toggleClass("active");
})





$(document).on('click', ".sort_col" ,function(){

    let column = $(this).data('column');
    let order = $(this).data('order');
    let sortedRows = [];

    const rows = Array.from(document.querySelectorAll(".row"));

    console.log("this click", column, order);

    let text = $(this).html();
    text = text.substring(0, text.length-1);


    if(order == "DESC"){
        $(this).data('order', "ASC");

        text = text + '&#x25BC';

        if(column == 1 || column == 5){
  
            sortedRows = rows.sort((a, b) => a.querySelectorAll("td")[column].textContent.toLowerCase() > b.querySelectorAll("td")[column].textContent.toLowerCase() ? -1 : 1);
        }else{

            sortedRows = rows.sort((a, b) => {

                aDate = convert_date(a.querySelectorAll("td")[column].textContent);
                bDate = convert_date(b.querySelectorAll("td")[column].textContent);

                if(aDate > bDate){
                    return -1;
                }else{
                    return 1;
                }
            });
            
        }


    }else{

        $(this).data('order', 'DESC');

        text = text + '&#x25B2';

        if(column == 1 || column == 5){

            //console.log(querySelectorAll("td")[column].textContent)
            
            sortedRows = rows.sort((a, b) => a.querySelectorAll("td")[column].textContent.toLowerCase() > b.querySelectorAll("td")[column].textContent.toLowerCase() ? 1 : -1);
        }else{

            sortedRows = rows.sort((a, b) => {

                aDate = convert_date(a.querySelectorAll("td")[column].textContent);
                bDate = convert_date(b.querySelectorAll("td")[column].textContent);

                if(aDate > bDate){
                    return 1;
                }else{
                    return -1;
                }
            });
        }

    }
    $(this).html(text);

    $("tbody").html(sortedRows);


});




// function sort(){

    
//     const rows = Array.from(document.querySelectorAll(".row"));
//     let column = $(this).data('column');
//     let order = $(this).data('order');

//     console.log("the button has click", column, order)

   
//     const sortedRows = rows.sort((a, b) => {

//         const aText = a.querySelectorAll("td")[1];
//         const bText = b.querySelectorAll("td")[1];


        

//         if(aText.textContent.toLocaleLowerCase() > bText.textContent.toLowerCase()){
//             return -1;
//         }

//         if(aText.textContent.toLowerCase() < bText.textContent.toLowerCase()){
//             return 1;
//         }

//         return 0;
//     })

//     $("tbody").html(sortedRows);



//   };




