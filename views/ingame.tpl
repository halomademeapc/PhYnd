% include('header.tpl', title="Play")
<nav class="breadcrumb">
    <a class="breadcrumb-item" href="/">phÿnd</a>
    <a class="breadcrumb-item" href="/play">play</a>
    <span class="breadcrumb-item active">{{gameid}}</span>
</nav>

<div class="ajaxBoard">
    <div class="spinner-layer spinner-green-only">
        <div class="circle-clipper left">
        <div class="circle"></div>
        </div>
        <div class="gap-patch">
        <div class="circle"></div>
        </div>
        <div class="circle-clipper right">
        <div class="circle"></div>
        </div>
    </div>
    <p>phÿnd is thinking...</p>
</div>

% #include ('footer.tpl')
<script>
    $(document).ready(function() {
        $(".ajaxBoard").load("/ajax/board/{{gameid}}/play")
    })
</script>