Crypto-Attack
Am creat o conexiune TCP cu ncat catre adresa din task. 
Am gasit informatii pe Wikipedia despre Diffie-Hellman Key exchange:
https://en.m.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange
Am creat o cheie privata si mi-am generat cu p di g cheia mea publica.
Am copiat-o in terminalul unde era deschisa conexiunea si am obtinut flagul criptat.
Am obtinut shared secretul din cheia publica a lui si secretul meu si am decriptat.

Linux-Acl
M-am conectat la: ssh -i ./id_rsa janitor@isc2023.1337.cx
Am gasit mai multe fisiere probabil lasa-te pentru hint.
Am observat ca fisierul robot-sudo imi da perimisiunile utilizatorului
iamrobot pentru /sbin/.secure/dir/elB0ss0 si /usr/local/bin/vacuum-control.
Am luat codul din fisierul /sbin/.secure/dir/elB0ss0 folosind comanda Strings.
Am dat copy fisierului vacuum-control pastrand prefixul.
Am rulat apoi robot-sudo /usr/local/bin/vacuum-control-v1 /sbin/.secure/dir/elB0ss0 
si apoi codul. Astfel am obtinut flagul.

Binary-exploit
Am decompilat folosind ghidra. Am observat functia loop ce contine un buffer de 33 de caractere.
Adresa functiei win in decimal: 0x80486e6 -> 134514406.
Payload sa ajung in win: 34 de 0 (dimensiune buffer + 1) + de cateva ori 0 + adresa functiei win.
Pentru payload-ul final am mai adaugat un 0 si lucky_number, intrucat am observat ca in win
se compara eax, registrul ce contine numarul cu esp+0x80 unde se pastreaza parametrul meu.
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 134514406 0 727 x
Intrucat se mai genereaza un lucky number dupa ce se declara inputul a mai fost nevoie sa fie 
suprascrisa adresa de return cu adresa lui loop, in felul acesta cand se dadea ca nu se mai 
continua nu se mai genera un nou lucky_number.
Adresa functie loop in decimal: 0x80487b3 -> 134514611
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 134514611 x
