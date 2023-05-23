# 4. Double linked list

## Delete a node at a specific index from a list

Please find here my implementation of a Double linked list in C: [source code](./https://github.com/holbertonschool/0x00-Fix_My_Code_Challenge/tree/master/4-delete_dnodeint)

Something is going wrong….
```
$ gcc -Wall -pedantic -Werror -Wextra -std=gnu89 main.c free_dlistint.c print_dlistint.c add_dnodeint_end.c delete_dnodeint_at_index.c -o delete_dnodeint
$ ./delete_dnodeint 
0
1
2
3
4
98
402
1024
-----------------
0
1
2
3
4
0
402
1024
-----------------
1
2
3
4
0
402
1024
-----------------
2
3
4
0
402
1024
-----------------
3
4
0
402
1024
-----------------
4
0
402
1024
-----------------
0
402
1024
-----------------
402
1024
-----------------
-----------------
-----------------
-----------------
-----------------
-----------------
-----------------
-----------------
-----------------
-----------------
$
```
It doesn’t look right…

## Fix

* Modify `if (0 == index)` to `if (index == 0)` to fix betty error on line `34`
* on line `46`, modify `(*head)->prev->prev = (*head)->prev;` to delete the next node instead of the previous by replacing with `(*head)->prev->next = (*head)->next;`
