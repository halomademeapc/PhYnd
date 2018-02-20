% include('header.tpl', title="Summary", subtitle="Summary of game " + gameid + " against phȳnd")


% if winner is None:
    <h3>The game ended in a draw</h3>
% end
% if winner == 'X':
    <h3>phȳnd wins!</h3>
% end
% if winner == 'O':
    <h3>you won!</h3>
% end

<div class="ajaxBoard">
    phȳnd is thinking...
</div>

<button id="newGameButton">New Game</button>

% #include ('footer.tpl')
<script>
    $(document).ready(function() {
        $(".ajaxBoard").load("/ajax/board/{{gameid}}/view")
    });
    $("#newGameButton").click(function() {
        window.location.href = "/play/new";
    });
</script>