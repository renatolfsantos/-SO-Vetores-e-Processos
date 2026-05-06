# -SO-Lista-Vetores-Processos
Exercícios sobre vetores e manipulação de processos em Python

<h2>1. Vetor [50] inteiro</h2>
<p>Criar e coletar um vetor <code>[50]</code> inteiro</p>
<p>Calcular e exibir:</p>
<ul>
  <li>A média dos valores entre <code>10</code> e <code>200</code></li>
  <li>A soma dos números ímpares</li>
</ul>

<h2>2. Vetor [100] inteiro</h2>
<p>Criar e coletar um vetor <code>[100]</code> inteiro</p>
<p>Calcular e exibir:</p>
<ul>
  <li>O maior e o menor valor</li>
  <li>A média dos valores</li>
</ul>

<h2>3. Vetor [30] real</h2>
<p>Criar e coletar um vetor <code>[30]</code> real</p>
<p>Calcular e exibir:</p>
<ul>
  <li>A média do grupo</li>
  <li>A quantidade de valores acima da média</li>
  <li>As posições dos valores abaixo da média</li>
</ul>

<h2>4. PING por Sistema Operacional</h2>
<p>Criar uma função que retorne o nome do Sistema Operacional</p>
<p>Criar um procedimento que:</p>
<ul>
  <li>Chame a função do SO</li>
  <li>Execute o comando <code>PING</code> com <code>10</code> iterações em <code>www.google.com.br</code></li>
  <li>Trate a saída conforme o SO:</li>
  <ul>
    <li>No Windows: extrair <code>Média = XXX ms</code></li>
    <li>No Linux: extrair <code>avg</code> (separado por <code>/</code>)</li>
  </ul>
  <li>Utilizar <code>split</code> para obter apenas o valor</li>
</ul>

<p>Comandos:</p>
<ul>
  <li>Windows: <code>ping -4 -n 10 www.google.com.br</code></li>
  <li>Linux: <code>ping -4 -c 10 www.google.com.br</code></li>
</ul>

<h2>5. Gerenciamento de Processos</h2>
<p>Criar uma aplicação que funcione em Linux e Windows</p>

<p>A <code>main</code> deve permitir entrada:</p>
<ul>
  <li><code>1</code> → listar processos</li>
  <li><code>2</code> → matar por PID</li>
  <li><code>3</code> → matar por nome</li>
  <li><code>9</code> → encerrar</li>
</ul>

<p>Criar uma função <code>os()</code> que retorna o nome do SO</p>
<p>Criar um procedimento para executar processos filhos conforme o SO</p>

<p>Regras:</p>
<ul>
  <li>Opção <code>1</code>: exibir processos ativos</li>
  <li>Opção <code>2</code>: solicitar PID e executar comando</li>
  <li>Opção <code>3</code>: solicitar nome do processo e executar comando</li>
</ul>

<p>Comandos:</p>
<ul>
  <li>Listar processos:</li>
  <ul>
    <li>Windows: <code>TASKLIST /FO TABLE</code></li>
    <li>Linux: <code>ps -ef</code></li>
  </ul>
  <li>Matar por PID:</li>
  <ul>
    <li>Windows: <code>TASKKILL /PID pid_do_processo</code></li>
    <li>Linux: <code>kill -9 pid_do_processo</code></li>
  </ul>
  <li>Matar por nome:</li>
  <ul>
    <li>Windows: <code>TASKKILL /IM nome_do_processo</code></li>
    <li>Linux: <code>pkill -f nome_do_processo</code></li>
  </ul>
</ul>
