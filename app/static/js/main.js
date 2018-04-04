// (function ($){
//   $(function () {
//     //initialize all modals
//      $('.modal').modal();
//
//      // var messages = "{{ get_flashed_messages() }}";
//      // if (typeof messages != 'undefined' && messages != '[]') {
//      //   Materialize.toast(messages,40);
//      // };
//
//      //now you can open modal from code
//      //$('#modal1').modal('open');
//
//      //or by click on trigger
//      $('.trigger-modal').modal();
//
//     }
//   // $(function(){}
// })(jQuery);

$(document).ready(function() {
    //All custom jQuery will go here:
    //Initialize All Modals:
    $(function () {
      //initialize all modals
      $('.modal').modal();

       // var messages = "{{ get_flashed_messages() }}";
       // if (typeof messages != 'undefined' && messages != '[]') {
       //   Materialize.toast(messages,40);
       // };

       //now you can open modal from code
       //$('#modal1').modal('open');

       //or by click on trigger
       $('.trigger-modal').modal();


     })
});

function modalCurrency(currencyID,modalID){
 $(modalID).modal('open');
};

function addCurrency(currencyID,modalID){
  $('button').click(function(e){
    $(modalID).modal('close');
    e.preventDefault();
    var amount = $("#money").val();
    $.post('/addCurrency',{
      currencyID: currencyID,
      currencyAmount:amount
    }).done(function(addCurrency){
      console.log(currencyID);
      console.log(amount);
      Materialize.toast('I have added a currency!', 4000) // 4000 is the duration of the toast
    }).fail(function(){
      console.log(currencyID);
      console.log(amount);
      console.log("I have FAILED");
      $(modalID).modal('close');
      Materialize.toast('I have failed to add a currency!', 4000) // 4000 is the duration of the toast
    })
   // return false;
  });
}
function removeCurrency(){

};
