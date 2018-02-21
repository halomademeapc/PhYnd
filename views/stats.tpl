% include('header.tpl', title="Stats", subtitle="Here are some numbers about how much time has been wasted thus far.")

<ul>
<li>phÿnd has played {{str(totalGames)}} games.</li>
<li>phÿnd has won {{str(totalWins)}} games and lost {{totalLosses}}.</li>
<li>phÿnd has made {{str(totalMoves)}} moves.</li>
<li>The average game lasts for {{str(avgMoves)}} moves.</li>
<li>Phynd has encountered {{str(scenarioCount)}} unique scenario and made adjustments to its likelihood to respond with {{str(outcomeCount)}} different responses for those states. </li>
</ul>
% #include ('footer.tpl')