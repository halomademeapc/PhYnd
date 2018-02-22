% include('header.tpl', title="Stats", subtitle="Here are some numbers about how much time has been wasted thus far.")
<nav class="breadcrumb">
    <a class="breadcrumb-item" href="/">phÿnd</a>
    <span class="breadcrumb-item active">stats</span>
</nav>
<div class="card-deck">
    <div class="card mb-4">
        <div class="card-body">
            <div class="statcircle bg-primary">
                <div class="statcontent align-middle">
                    <div class="text-white number">{{str(totalGames)}}</div>
                    <div class="text-light statico">
                        <i class="fas fa-check"></i>
                    </div>
                </div>
            </div>
            <p class="card-text text-center">phÿnd has played {{str(totalGames)}} games</p>
        </div>
    </div>

    <div class="card mb-4">
        <div class="card-body">
            <div class="statcircle bg-secondary">
                <div class="statcontent align-middle">
                    <div class="text-white number">{{str(totalWins)}}</div>
                    <div class="text-light statico">
                        <i class="fas fa-trophy"></i>
                    </div>
                </div>
            </div>
            <p class="card-text text-center">phÿnd has won {{str(totalWins)}} games and lost {{totalLosses}}</p>
        </div>
    </div>

    <div class="card mb-4">
        <div class="card-body">
            <div class="statcircle bg-success">
                <div class="statcontent align-middle">
                    <div class="text-white number">{{str(totalMoves)}}</div>
                    <div class="text-light statico">
                        <i class="fas fa-expand-arrows-alt"></i>
                    </div>
                </div>
            </div>
            <p class="card-text text-center">phÿnd has made {{str(totalMoves)}} moves</p>
        </div>
    </div>
</div>
<div class="card-deck">
    <div class="card mb-4">
        <div class="card-body">
            <div class="statcircle bg-info">
                <div class="statcontent align-middle">
                    <div class="text-white number">{{str(avgMoves)}}</div>
                    <div class="text-light statico">
                        <i class="far fa-chart-bar"></i>
                    </div>
                </div>
            </div>
            <p class="card-text text-center">The average game lasts for {{str(avgMoves)}} moves.</p>
        </div>
    </div>

    <div class="card mb-4">
        <div class="card-body">
            <div class="statcircle bg-dark">
                <div class="statcontent align-middle">
                    <div class="text-white number">{{str(scenarioCount)}}</div>
                    <div class="text-light statico">
                        <i class="fas fa-binoculars"></i>
                    </div>
                </div>
            </div>
            <p class="card-text text-center">phÿnd has encountered {{str(scenarioCount)}} unique scenarios and made adjustments to its likelihood to respond
                with {{str(outcomeCount)}} different responses for those states.</p>
        </div>
    </div>

</div>
% #include ('footer.tpl')