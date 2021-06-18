 <?php
 if(!isset($_SESSION)) 
    { 
        session_start(); 
    } 
?>
<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <!--Import materialize.css-->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.98.2/css/materialize.min.css">
    <!--Import Google Icon Font-->
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">

    <!--Let browser know website is optimized for mobile-->
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" type="text/css" href="css/style.css" media="screen">

    <title>강민석짱짱맨</title>
</head>
<body>
    <div id="root">

        <!-- Modal Trigger -->
        <!-- Modal Structure -->

        <div id="modal1" class="modal">
          <div class="modal-content">
            <h4>변경완료</h4>
            <p>알림이 변경되었습니다.</p>
          </div>
          <div class="modal-footer">
            <a href="#!" class="modal-action modal-close waves-effect waves-green btn-flat">확인</a>
          </div>
        </div>

        <nav>
            <div class="nav-wrapper">
                <a href="#" class="brand-logo">스케쥴관리 로그인</a>
            </div>
        </nav>
        <div class="row" style ="margin-top:20%">
          <form class="col s12" action = "DB/logincheck.php" method ="POST" >
              <div class="input-field col s12">
                <input placeholder="종정시 학번" id="first_name" type="text" class="validate" name = "username">
                <label for="first_name">ID</label>
              </div>
              <div class="input-field col s12">
                <input id="password" type="password" class="validate" name = "userpw">
                <label for="password">Password</label>
              </div>
            <button class="btn waves-effect waves-light col s12" type="submit" name="action">로그인
              <i class="material-icons right">send</i>
            </button>
          </form>
        </div>


    </div>
    <!--script type="text/javascript" src="https://code.jquery.com/jquery-2.1.1.min.js"></script-->
    <script src="http://code.jquery.com/jquery-1.11.1.min.js"></script>
    <script src="js/jquery.form.min.js"></script>



    <!-- Compiled and minified JavaScript -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.98.2/js/materialize.min.js"></script>
    <script>
        $(document).ready(function() {
          function goForm(){
          //alert("gdgddg");
          document.form2.submit();
          }
             $('ul.tabs').tabs();
            $('select').material_select();
            $('.chips').material_chip();
            $('.chips-placeholder').material_chip({
                placeholder: 'Enter a tag',
                secondaryPlaceholder: '+Tag',
            });

            $('.carousel.carousel-slider').carousel({
                fullWidth: true
            });

            var datepic = $('.datepicker').pickadate({
                selectMonths: true, // Creates a dropdown to control month
                selectYears: 2, // Creates a dropdown of 15 years to control year
                format: 'yyyy-mm-dd'
            });
            var picker = datepic.pickadate('picker');
            picker.set('select', new Date(Date.now()));

            $('.chips').on('chip.add', function(e, chip) {
                console.log($('.chips-placeholder').material_chip('data').length);
                console.log(
                    Object.values(
                        $('.chips-placeholder').material_chip('data')
                    )
                );
            });
            $('.modal').modal();
            <% if(success) { %>
                $('#modal1').modal('open');
            <% }%>

        });
    </script>
</body>

</html>
