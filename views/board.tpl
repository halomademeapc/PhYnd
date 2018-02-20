<table class="board">
% pos = 0
% for x in range(0,3):
    <tr>
    % for y in range(0,3):
        <td>
        % if(interact and (state[pos] == '-')): 
            <a href="/play/{{gameid}}/{{pos}}">
        % end
            <div class="boarditem">
                {{state[pos]}}
            </div>
        % if(interact and (state[pos] == '-')): 
            </a>
        % end
        </td>
    % pos += 1
    % end
    </tr>
% end
</table>