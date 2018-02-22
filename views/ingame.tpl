% include('header.tpl', title="Play")
<nav class="breadcrumb">
    <a class="breadcrumb-item" href="/">phÿnd</a>
    <a class="breadcrumb-item" href="/play">play</a>
    <span class="breadcrumb-item active">{{gameid}}</span>
</nav>

<div class="ajaxBoard text-center">
    <svg class="spinner center-block" width="65px" height="65px" viewBox="0 0 66 66" xmlns="http://www.w3.org/2000/svg">
        <circle class="path" fill="none" stroke-width="6" stroke-linecap="round" cx="33" cy="33" r="30"></circle>
    </svg>
    <p class="text-center">phÿnd is thinking...</p>
</div>

% #include ('footer.tpl')
<script>
    $(document).ready(function () {
        $(".ajaxBoard").load("/ajax/board/{{gameid}}/play")
    })
</script>