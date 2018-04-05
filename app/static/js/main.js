$(document).ready(function() {
    //All custom jQuery will go here:
    //Initialize All Modals:
    $(function () {
      //initialize all modals
      $('.modal').modal();

       //now you can open modal from code
       //$('#modal1').modal('open');

       //or by click on trigger
       $('.trigger-modal').modal();


     })
});

function modalCurrency(currencyID,modalID){
 $(modalID).modal('open');
};

function addCurrency(currencyID,modalID,symbol){
  $(modalID).modal('close');
  var amount = $(modalID).find('#money').val();
  $.post('/addCurrency',{
    currencyID: currencyID,
    currencyAmount:amount,
    currencySymbol:symbol
  }).done(function(addCurrency){
    Materialize.toast('I have added a currency!', 4000) // 4000 is the duration of the toast
  }).fail(function(){
    $(modalID).modal('close');
    Materialize.toast('I have failed to add a currency! This currency has already been added!', 4000) // 4000 is the duration of the toast
  })
  return false;
};

function updateCurrency(currencyID,modalID){
  console.log("updateCurrency Called");
  $(modalID).modal('close');
  var amount = $(modalID).find('#money').val();
  $.post('/updateCurrency',{
    currencyID:currencyID,
    currencyAmount:amount,
    status:"update"
  }).done(function(updateCurrency){
    Materialize.toast('I have updated the currency amount!', 4000) // 4000 is the duration of the toast
  }).fail(function(){
    Materialize.toast('I have failed to update the currency!', 4000) // 4000 is the duration of the toast
  })
  console.log(currencyID);

  $("#li"+currencyID).find("p > #money").text(amount);
  return false;
};

function removeCurrency(currencyID,modalID){
  console.log("removeCurrency Called");
  $('#delete'+modalID).modal('open');
  $('#confirmDelete'+currencyID).click(function(){
    $('#delete'+modalID).modal('close');
    $.post('/updateCurrency',{
      currencyID:currencyID,
      status:"delete"
    }).done(function(removeCurrency){
      Materialize.toast('I have deleted the currency!', 4000) // 4000 is the duration of the toast
    }).fail(function(){
      Materialize.toast('I have failed to delete the currency!', 4000) // 4000 is the duration of the toast
    })
  });
  $('#li'+currencyID).remove();
  return false;
};
