// $(document).ready(function () {
//   $('.modal').modal();
//   $('#modal1').on('click',function(){
//
//   });
// });

(function ($){
  $(function () {
    //initialize all modals
     $('.modal').modal();

     //now you can open modal from code
     // $('#modal1').modal('open');

     //or by click on trigger
     $('.trigger-modal').modal();
  })
})(jQuery);
