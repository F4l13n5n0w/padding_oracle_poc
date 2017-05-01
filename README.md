# padding_oracle_poc
This is a python code, used to demo the PoC of padding oracle exploit

## Why this
This is an Exercise of Capture-The-Flag Badge which is created by PentesterLab. The best way to get a better understanding of Padding Oracle attack is to write a PoC code by yourself.

## Limitations
In this rough version, only demo using padding oracle attack to encrypt arbitary plain text (`user=admin` in this case) to grab Admin priviledge.

## Notes
In this case, the plaintext is `user=admin`, the result as follow:ls

```
** Finished **
[+] Encrypted value is: vsyeuh1661RtW8u/SsuqHQAAAAAAAAAA
```



## Reference
[1] PentesterLab CTF Badge exercise: [Padding Oracle][1]
[2] OWASP Testing guide: [OTG-CRYPST-002][3]
[3] Testing tool: [PadBuster][2]



<!--- Reference -->

[1]: https://pentesterlab.com/exercises/padding_oracle/course							"Padding Oracle - PentesterLab"
[2]: https://github.com/GDSSecurity/PadBuster											"PadBuster"
[3]: https://www.owasp.org/index.php/Testing_for_Padding_Oracle_(OTG-CRYPST-002)		"OWASP Testing guide"
