(function ($){
  $(function () {
    //initialize all modals
     $('.modal').modal();

     // var messages = "{{ get_flashed_messages() }}";
     // if (typeof messages != 'undefined' && messages != '[]') {
     //   Materialize.toast(messages,40);
     // };

     //now you can open modal from code
     // $('#modal1').modal('open');

     //or by click on trigger
     $('.trigger-modal').modal();

  })
})(jQuery);
