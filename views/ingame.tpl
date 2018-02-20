% include('header.tpl', title="Play", subtitle="You are playing game " + gameid + " against phȳnd")

<div class="ajaxBoard">
    phȳnd is thinking...
</div>

% #include ('footer.tpl')
<script>
    $(document).ready(function() {
        $(".ajaxBoard").load("/ajax/board/{{gameid}}/play")
    })
</script>