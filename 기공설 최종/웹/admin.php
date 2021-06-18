 <?php
 if(!isset($_SESSION)) 
    { 
        session_start(); 
    } 
  $id = $_GET['id'];
  require_once("DB/dbconfig.php");
  $result = mysqli_query($db,"SELECT * FROM lecture where id = ".$id.";");
  //echo "<script>alert('$id');</script>";
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
        <?
        while($row = mysqli_fetch_array($result)){
          echo '<div class="row">';
          echo '<div class="col s12 m6">';
            echo '<div class="card blue-grey darken-1">';
            echo '  <div class="progress"><div class="indeterminate"></div></div>';
              echo '<div class="card-content white-text">';
                echo '<span class="card-title">'.$row['name']."-".$row['propessor'].'</span>';
                echo '<p>'.$row['day']." - ".$row['starttime']." ~ ".$row['endtime']." - ".$row['location'].'</p>';
              echo '</div>';
              echo '<div class="card-action">';
                echo '<div class="switch">';
                  echo '<label>';
                    echo 'Off';
                    if ( $row['flag'] == 'Y')
                    {
                      echo '<input type="checkbox" class ="" checked="checked" onchange="change('.$row['idx'].')">';
                    }
                    else{
                      echo '<input type="checkbox" class ="" onchange="change('.$row['idx'].')">';
                    }
                    echo '<span class="lever"></span>';
                    echo 'On';
                  echo '</label>';
                echo '</div>';
              echo '</div>';
              echo '<div class="card-action">';
                 echo '<div class="input-field s6" style = "width:50%">';
                    echo '<select name="hour" onchange="changehour(this.value,'.$row['idx'].');">';
                      echo '<option value="" disabled selected>'.$row['beforehour'].'</option>';
                      for($i = 1; $i <=12; $i++ )
                        echo '<option value='.$i.'>'.$i.'</option>';
                      
                    echo '</select>';
                    echo '<label>시간</label>';
                  echo '</div>';
                  echo '<div class="input-field s6" style = "width:50%">';
                    echo '<select name="minute" onchange="changeminute(this.value,'.$row['idx'].');">';
                      echo '<option value="" disabled selected>'.$row['beforeminute'].'</option>';
                      for($i = 0; $i <=59; $i++ )
                      echo '<option value='.$i.'>'.$i.'</option>';
                    echo '</select>';
                    echo '<label>분</label>';
                  echo '</div>';
                echo '</div>';
            echo '</div>';

          echo '</div>';
        echo '</div>';
        }
          
        mysqli_close($db);
        ?>

  
    </div>
    <!--script type="text/javascript" src="https://code.jquery.com/jquery-2.1.1.min.js"></script-->
    <script src="http://code.jquery.com/jquery-1.11.1.min.js"></script>
    <script src="js/jquery.form.min.js"></script>



    <!-- Compiled and minified JavaScript -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.98.2/js/materialize.min.js"></script>
    <script>
    function changehour(_var,_idx){
      //alert(_idx);
      //alert(_var);
        $.ajax({
          type: "GET", // POST형식으로 폼 전송
          url: "DB/modifyhour.php", // 목적지
          data: ({idx: _idx,hour:_var}),
          dataType: "text",
          success: function(data) {
            alert("시간변경완료");
          },
          error: function(xhr, textStatus, errorThrown) { // 전송 실패
            alert("전송에 실패했습니다.");
          }
        });
    }
    function changeminute(_var,_idx){
      $.ajax({
          type: "GET", // POST형식으로 폼 전송
          url: "DB/modifymin.php", // 목적지
          data: ({idx: _idx,min:_var}),
          dataType: "text",
          success: function(data) {
            alert("분변경완료");
          },
          error: function(xhr, textStatus, errorThrown) { // 전송 실패
            alert("전송에 실패했습니다.");
          }
        });
    }
    function change(_var) {
      //alert(_var);
        $.ajax({
          type: "GET", // POST형식으로 폼 전송
          url: "DB/modifyalarm.php", // 목적지
          data: ({idx: _var}),
          dataType: "text",
          success: function(data) {
            alert("변경완료");
          },
          error: function(xhr, textStatus, errorThrown) { // 전송 실패
            alert("전송에 실패했습니다.");
          }
        }); 
      }
        $(document).ready(function() {

          $('select').material_select();
      
          $('.modal').modal();
            $('.modaltest').click(function(){
            $('#modal1').modal('open');
          })

        });
    </script>
</body>

</html>
