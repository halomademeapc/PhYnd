% include('header.tpl', title="About phÿnd", subtitle="It's just a school assignment, bro.")

<p>Looks like it's time for a new game.</p>
<button id="newGameButton">New Game</button>

% #include ('footer.tpl')
<script>
    $("#newGameButton").click(function() {
        window.location.href = "/play/new";
    });
</script>