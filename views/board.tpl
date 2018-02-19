<table class="board">
% for x in range(0,3):
    <tr>
    % for y in range(0,3):
        <td>
        % if(interactive): 
            <a href="#">
        % end
            <div class="boarditem">
                {{x}}{{y}}
            </div>
        % if(interactive): 
            </a>
        % end
        </td>
    % end
    </tr>
% end
</table>