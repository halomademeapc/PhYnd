% include('header.tpl', title="Summary", subtitle="Summary of game " + gameid + " against phÿnd")
<nav class="breadcrumb">
    <a class="breadcrumb-item" href="/">phÿnd</a>
    <a class="breadcrumb-item" href="/play">play</a>
    <a href="/play/{{gameid}}" class="breadcrumb-item">{{gameid}}</a>
    <span class="breadcrumb-item active">results</span>
</nav>

<div class="col-lg-4 col-md-6 mb-4">

    <!--Card-->
    <div class="card card-cascade narrower">

        <div class="view overlay">
            <div class="ajaxBoard">
                
                loading results
            </div>
        </div>

        <div class="card-body">
            <h4 class="card-title">
                % if winner is None:
                The game ended in a draw
                % end 
                % if winner == 'X':
                phÿnd wins!
                % end 
                % if winner == 'O':
                You won!
                % end
            </h4>
            <p class="card-text">Thanks for playing! Your contribution probably won't help mankind's advancement, but hopefully it was at least a little fun.</p>
            <a class="btn btn-unique waves-effect waves-light" href="/play/new">Play again</a>
        </div>

    </div>
</div>

% #include ('footer.tpl')
<script>
    $(document).ready(function () {
        $(".ajaxBoard").load("/ajax/board/{{gameid}}/view")
    });
</script>