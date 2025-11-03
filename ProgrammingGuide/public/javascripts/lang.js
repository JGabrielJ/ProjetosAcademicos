let html = document.getElementById("html");
let javascript = document.getElementById("javascript");
let python = document.getElementById("python");
let cpp = document.getElementById("cpp");
let kotlin = document.getElementById("kotlin");
let markdown = document.getElementById("markdown");

html.addEventListener("click", () => {
    const content = document.getElementById("languages");
    content.innerHTML = `
        <h1> HTML/CSS </h1>
		<p> HTML (HyperText Markup Language) e CSS (Cascading Style Sheets) são duas linguagens que permitem criar e estilizar páginas web. HTML define a estrutura e o conteúdo de uma página, enquanto CSS define a aparência e o layout. </p>

        <p> Usar HTML e CSS é essencial para desenvolver sites modernos, responsivos e acessíveis. HTML e CSS permitem criar páginas que se adaptam a diferentes dispositivos, tamanhos de tela e resoluções. Além disso, HTML e CSS seguem padrões internacionais que garantem a compatibilidade e a interoperabilidade entre diferentes navegadores e plataformas. </p>

        <p> As principais funcionalidades do HTML são: criar elementos que representam o conteúdo de uma página, como títulos, parágrafos, listas, imagens, links, formulários, etc.; organizar os elementos em uma hierarquia lógica, usando tags que indicam o início e o fim de cada elemento; e atribuir atributos aos elementos, que fornecem informações adicionais sobre eles, como id, class, src, href, etc. E as principais funcionalidades do CSS são: selecionar os elementos do HTML que serão estilizados, usando seletores que podem ser baseados em tags, atributos, classes, ids, pseudo-classes, pseudo-elementos, etc.; aplicar propriedades aos elementos selecionados, que definem aspectos como cores, fontes, bordas, margens, espaçamentos, alinhamentos, posicionamentos, animações, transições, etc.; e agrupar as propriedades em regras, que podem ser escritas em um arquivo externo, em um elemento style dentro do HTML ou em um atributo style dentro de cada elemento. </p>

        <h2> Vantagens </h2>
        <ul>
            <li><strong>Facilidade de aprendizado e uso.</strong></li>
            <li><strong>Flexibilidade e criatividade na criação de páginas web.</strong></li>
            <li><strong>Separação entre conteúdo e apresentação.</strong></li>
            <li><strong>Controle sobre o design e a usabilidade das páginas.</strong></li>
            <li><strong>Possibilidade de reutilização e manutenção do código.</strong></li>
        </ul><br>

        <h2> Desvantagens </h2>
        <ul>
            <li><strong>Necessidade de testar as páginas em diferentes navegadores e dispositivos.</strong></li>
            <li><strong>Limitações na interatividade e na funcionalidade das páginas.</strong></li>
            <li><strong>Dependência de frameworks e bibliotecas para implementar recursos avançados.</strong></li>
            <li><strong>Diferenças entre as versões e as especificações do HTML e do CSS.</strong></li>
        </ul><br>

        <p> O contêiner abaixo mostra um exemplo de código feito em HTML (o CSS é o &lt;style&gt;). </p>
        <div class="example">
            <p class="code">
                &lt;!<span class="comp">DOCTYPE</span> <span class="var">html</span>&gt;<br>
				&lt;<span class="comp">html</span> <span class="var">lang</span>=<span class="str">"pt-BR"</span>&gt;<br>
					<span class="indent">&lt;<span class="comp">head</span>&gt;</span><br>
						<span class="indent"><span class="indent">&lt;<span class="comp">meta</span> <span class="var">charset</span>=<span class="str">"UTF-8"</span>&gt;</span></span><br>
						<span class="indent"><span class="indent">&lt;<span class="comp">meta</span> <span class="var">http-equiv</span>=<span class="str">"X-UA-Compatible"</span> <span class="var">content</span>=<span class="str">"IE=edge"</span>&gt;</span></span><br>
						<span class="indent"><span class="indent">&lt;<span class="comp">meta</span> <span class="var">name</span>=<span class="str">"viewport"</span> <span class="var">content</span>=<span class="str">"width=device-width, initial-scale=1.0"</span>&gt;</span></span><br>
						<span class="indent"><span class="indent">&lt;<span class="comp">title</span>&gt; Exemplo &lt;\/<span class="comp">title</span>&gt;</span></span><br>
						<span class="indent"><span class="indent">&lt;<span class="comp">style</span>&gt;</span></span><br>
							<span class="indent"><span class="indent"><span class="indent"><span class="func">body</span> <span class="chav">{</span></span></span></span><br>
								<span class="indent"><span class="indent"><span class="indent"><span class="indent"><span class="var">color</span>: <span class="str">black</span>;</span></span></span></span><br>
								<span class="indent"><span class="indent"><span class="indent"><span class="indent"><span class="var">background-color</span>: <span class="str">white</span>;</span></span></span></span><br>
							<span class="indent"><span class="indent"><span class="indent"><span class="chav">}</span></span></span></span><br>
						<span class="indent"><span class="indent">&lt;\/<span class="comp">style</span>&gt;</span></span><br>
					<span class="indent">&lt;\/<span class="comp">head</span>&gt;</span><br><br>
					<span class="indent">&lt;<span class="comp">body</span>&gt;</span><br>
						<span class="indent"><span class="indent">&lt;<span class="comp">h1</span>&gt; Hello, World! &lt;\/<span class="comp">h1</span>&gt;</span></span><br>
					<span class="indent">&lt;\/<span class="comp">body</span>&gt;</span><br>
				&lt;\/<span class="comp">html</span>&gt;<br>
            </p>
        </div>
    `;
});

javascript.addEventListener("click", () => {
    const content = document.getElementById("languages");
    content.innerHTML = `
        <h1> JavaScript </h1>
		<p> JavaScript é uma linguagem de programação que permite criar páginas web dinâmicas e interativas. Ela é executada no navegador do usuário, sem a necessidade de um servidor web. JavaScript é uma linguagem versátil, que pode ser usada para diversos fins, como manipular elementos do HTML, validar formulários, criar animações, desenvolver jogos e aplicações web. </p>

        <p> Uma das razões para usar JavaScript é que ela é uma linguagem fácil de aprender e de usar. Ela tem uma sintaxe simples e clara, que se assemelha à linguagem natural. Além disso, JavaScript é uma linguagem interpretada, o que significa que não precisa ser compilada antes de ser executada. Isso torna o processo de desenvolvimento mais rápido e flexível. Outra razão para usar JavaScript é que ela é uma linguagem universal, que pode ser usada em diferentes plataformas e dispositivos. Ela é compatível com a maioria dos navegadores web e pode se comunicar com outras linguagens, como PHP, Java e Python. </p>

        <p> As principais funcionalidades de JavaScript são as funções (blocos de código que podem ser reutilizados em diferentes partes do programa; elas permitem modularizar o código e torná-lo mais organizado e legível. As funções podem receber parâmetros e retornar valores), os objetos (estruturas de dados que agrupam propriedades e métodos relacionados a um determinado conceito ou entidade; eles permitem representar dados complexos e abstratos de forma mais natural e intuitiva; os objetos podem ser criados a partir de classes ou de forma literal), os eventos (ações que ocorrem no navegador, como cliques, movimentos do mouse, teclas pressionadas, etc.; eles permitem capturar a interação do usuário com a página web e responder a ela de forma adequada; os eventos podem ser tratados por meio de funções chamadas de callbacks ou listeners) e a DOM (a sigla para Document Object Model, que é a representação hierárquica dos elementos do HTML em forma de objetos; o DOM permite acessar e modificar os elementos da página web por meio de JavaScript, alterando seu conteúdo, estilo e comportamento). </p>

        <h2> Vantagens </h2>
        <ul>
            <li><strong>Popularidade:</strong> É uma linguagem popular e amplamente usada no desenvolvimento web. </li>
            <li><strong>Flexibilidade:</strong> É uma linguagem flexível e adaptável, que permite criar diferentes tipos de aplicações web. </li>
            <li><strong>Interação e dinamicidade:</strong> É uma linguagem que oferece muitas possibilidades de interatividade e dinamismo na página web. </li>
            <li><strong>Comunidade ativa:</strong> É uma linguagem que tem uma grande comunidade de desenvolvedores e uma vasta documentação disponível. </li>
        </ul><br>

        <h2> Desvantagens </h2>
        <ul>
            <li><strong>Inconsistência:</strong> É uma linguagem que pode apresentar inconsistências e incompatibilidades entre os diferentes navegadores web. </li>
            <li><strong>Vulnerabilidade:</strong> É uma linguagem que pode ser vulnerável a ataques maliciosos, como injeção de código ou roubo de dados. </li>
            <li><strong>Desempenho:</strong> É uma linguagem que pode ter problemas de desempenho e eficiência, especialmente em aplicações web complexas ou pesadas. </li>
            <li><strong>Complexidade:</strong> É uma linguagem que pode gerar código confuso e difícil de manter, se não for bem estruturada e organizada. </li>
        </ul><br>

        <p> O contêiner abaixo mostra um exemplo de código feito na linguagem JavaScript. </p>
        <div class="example">
            <p class="code">
                <span class="comp">let</span> <span class="var">numbers</span> = [<span class="num">2</span>, <span class="num">4</span>, <span class="num">6</span>, <span class="num">8</span>];<br>
                <span class="comp">let</span> <span class="var">product</span> = <span class="num">1</span>;<br>
                <span class="command">for</span> (<span class="comp">let</span> <span class="var">num</span> <span class="comp">in</span> <span class="var">numbers</span>) {<br>
                <span class="indent"><span class="var">product</span> *= <span class="var">num</span></span>;<br>
				}<br><br>
                <span class="var">console</span>.<span class="func">log</span>(<span class="str">\`The product is <span class="comp">$</span><span class="command">{<span class="var">product</span>}</span>.\`</span>);
            </p>
        </div>
    `;
});

python.addEventListener("click", () => {
    const content = document.getElementById("languages");
    content.innerHTML = `
        <h1> Python </h1>
        <p> Python é uma linguagem de programação de alto nível, interpretada, multiparadigma e de propósito geral. Foi criada por Guido van Rossum em 1991 e é amplamente utilizada em diversos domínios, como desenvolvimento web, ciência de dados, inteligência artificial e automação. </p>

        <p> Uma das razões para usar Python é a sua simplicidade e legibilidade, que facilitam a escrita e a manutenção de código. Além disso, Python possui uma grande comunidade de desenvolvedores e uma vasta biblioteca padrão, que oferece módulos para diversas tarefas comuns, como manipulação de arquivos, expressões regulares, interface gráfica e testes automatizados. </p>

        <p> Entre as principais funcionalidades da linguagem Python, podemos destacar a tipagem dinâmica, que permite atribuir valores de diferentes tipos a uma mesma variável, sem a necessidade de declarar o tipo explicitamente; a indentação obrigatória, que define o escopo dos blocos de código pela quantidade de espaços à esquerda, tornando o código mais organizado e consistente; o suporte a múltiplos paradigmas de programação, como o imperativo, o orientado a objetos, o funcional e o procedural; e a possibilidade de estender e integrar Python com outras linguagens, como C, C++, Java e .NET, através de mecanismos como ctypes, SWIG e Jython. </p>

        <h2> Vantagens </h2>
        <ul>
            <li><strong>Facilidade de aprendizado:</strong> A facilidade de aprendizado e uso, especialmente para iniciantes. </li>
            <li><strong>Portabilidade:</strong> A portabilidade e a compatibilidade entre diferentes plataformas e sistemas operacionais. </li>
            <li><strong>Produtividade:</strong> A produtividade e a rapidez no desenvolvimento de aplicações complexas. </li>
            <li><strong>Diversidade de recursos:</strong> A riqueza e a diversidade de recursos disponíveis na biblioteca padrão e em pacotes externos. </li>
        </ul><br>

        <h2> Desvantagens </h2>
        <ul>
            <li><strong>Lentidão:</strong> Menor velocidade de execução em relação a linguagens compiladas, como C e C++. </li>
            <li><strong>Depuração complicada:</strong> A dificuldade de depuração e otimização de código, devido à tipagem dinâmica e à falta de ferramentas adequadas. </li>
            <li><strong>Incompatibilidade:</strong> A incompatibilidade entre as versões 2 e 3 da linguagem, que podem gerar problemas de migração e manutenção de código. </li>
            <li><strong>Dificuldades para desenvolver aplicações mobile:</strong> A menor oferta de empregos e salários em relação a outras linguagens mais populares no mercado. </li>
        </ul><br>

        <p> O contêiner abaixo mostra um exemplo de código feito na linguagem Python. </p>
        <div class="example">
            <p class="code">
                <span class="var">numbers</span> = [<span class="num">2</span>, <span class="num">4</span>, <span class="num">6</span>, <span class="num">8</span>]<br>
                <span class="var">product</span> = <span class="num">1</span><br>
                <span class="command">for</span> <span class="var">num</span> <span class="comp">in</span> <span class="var">numbers</span>:<br>
                <span class="indent"><span class="var">product</span> *= <span class="var">num</span></span><br><br>
                <span class="func">print</span>(<span class="comp">f</span><span class="str">'The product is <span class="command">{<span class="var">product</span>}</span>.'</span>)
            </p>
        </div>
    `;
});

cpp.addEventListener("click", () => {
    const content = document.getElementById("languages");
    content.innerHTML = `
        <h1> C++ </h1>
		<p> C++ é uma linguagem de programação de propósito geral, que suporta múltiplos paradigmas, como a programação orientada a objetos, a programação genérica e a programação funcional. Ela é uma extensão da linguagem C, que foi criada em 1972 por Dennis Ritchie. </p>

        <p> Uma das razões para usar C++ é a sua eficiência e desempenho, pois permite um controle fino sobre o uso de recursos como memória e processamento. Além disso, C++ é uma linguagem amplamente usada e reconhecida, que possui uma grande comunidade de desenvolvedores e uma vasta biblioteca padrão, chamada STL (Standard Template Library). </p>

        <p> Algumas das principais funcionalidades de C++ são a sobrecarga de operadores, que permite definir o comportamento de operadores como +, -, *, / para tipos definidos pelo usuário, como classes e estruturas; a herança múltipla, que permite que uma classe derive de mais de uma classe base, herdando os seus atributos e métodos; os templates, que permitem escrever código genérico que pode ser usado com diferentes tipos de dados, sem precisar repetir o código para cada tipo; e as exceções, que são mecanismos para lidar com situações de erro ou anormais, lançando e capturando objetos que representam o problema ocorrido. </p>

        <h2> Vantagens </h2>
        <ul>
            <li><strong>Compatibilidade:</strong> É compatível com a linguagem C, que facilita a integração com código legado ou bibliotecas escritas em C. </li>
            <li><strong>Portabilidade:</strong> C++ permite compilar e executar programas em diferentes plataformas e sistemas operacionais. </li>
            <li><strong>Flexibilidade:</strong> A linguagem permite escolher o paradigma de programação mais adequado para cada problema ou situação. </li>
            <li><strong>Expressividade:</strong> C++ permite escrever código conciso e elegante, usando recursos como os operadores sobrecarregados e os templates. </li>
        </ul><br>

        <h2> Desvantagens </h2>
        <ul>
            <li><strong>Complexidade:</strong> A linguagem é difícil de aprender e dominar, exigindo um conhecimento profundo dos seus conceitos e detalhes. </li>
            <li><strong>Falta de segurança:</strong> Isso pode levar a erros graves ou vulnerabilidades, como o estouro de buffer ou o vazamento de memória. </li>
            <li><strong>Inconsistência:</strong> Resulta da evolução da linguagem ao longo dos anos, gerando incompatibilidades entre as diferentes versões ou padrões. </li>
            <li><strong>Verbosidade:</strong> Pode tornar o código difícil de ler ou manter, especialmente quando se usa recursos como as macros ou os ponteiros. </li>
        </ul><br>

        <p> O contêiner abaixo mostra um exemplo de código feito na linguagem C++ (para Arduíno). </p>
        <div class="example">
            <p class="code">
                <span class="str">// C++ code</span><br><br>
                <span class="num">void</span> <span class="func">setup</span>() {<br>
                <span class="indent"><span class="func">pinMode</span>(<span class="num">3</span>, OUTPUT);</span></span><br>
				}<br><br>
                <span class="num">void</span> <span class="func">loop</span>() {<br>
                <span class="indent"><span class="func">digitalWrite</span>(<span class="num">3</span>, HIGH);</span><br>
                <span class="indent"><span class="func">delay</span>(<span class="num">10</span>);</span><br>
                <span class="indent"><span class="func">digitalWrite</span>(<span class="num">3</span>, LOW);</span><br>
                <span class="indent"><span class="func">delay</span>(<span class="num">10</span>);</span><br>
				}<br>
            </p>
        </div>
    `;
});

kotlin.addEventListener("click", () => {
    const content = document.getElementById("languages");
    content.innerHTML = `
        <h1> Kotlin </h1>
		<p> Kotlin é uma linguagem de programação moderna, concisa e segura, que roda na máquina virtual Java (JVM) e pode ser usada para desenvolver aplicativos para Android, web, desktop e outros. Ela foi criada pela JetBrains em 2011 e se tornou oficialmente suportada pelo Google para o desenvolvimento Android em 2017. </p>

        <p> Uma das principais razões para usar Kotlin é a sua interoperabilidade com Java, ou seja, é possível misturar código Kotlin e Java no mesmo projeto, aproveitando as bibliotecas e frameworks existentes. Além disso, Kotlin oferece vários recursos que tornam o código mais expressivo, conciso e seguro, como inferência de tipos, funções de ordem superior, null-safety, classes de dados, delegação de propriedades, corrotinas e muito mais. </p>

        <p> Entre as principais funcionalidades de Kotlin, podemos destacar o suporte a paradigmas de programação funcional e orientada a objetos, permitindo escrever código mais flexível e reutilizável; o suporte à programação multiplataforma, possibilitando compartilhar código entre diferentes plataformas, como Android, iOS, web, desktop e nativo; o suporte à programação assíncrona e não bloqueante, através das corrotinas, que são uma forma de escrever código concorrente de maneira simples e eficiente; e o suporte à metaprogramação, através de recursos como reflexão, anotações e DSLs (Domain Specific Languages), que permitem manipular e gerar código em tempo de execução ou compilação. </p>

        <h2> Vantagens </h2>
        <ul>
            <li><strong>Sintaxe:</strong> Simples e intuitiva, que facilita a leitura e a escrita do código. </li>
            <li><strong>Compatibilidade com Java:</strong> Permite aproveitar o vasto ecossistema de ferramentas e bibliotecas existentes. </li>
            <li><strong>Menos verbosidade:</strong> Menos código boilerplate, que reduz a verbosidade e a repetição do código. </li>
            <li><strong>Maior segurança:</strong> Evita erros comuns como NullPointerExceptions e bugs de concorrência. </li>
            <li><strong>Maior produtividade:</strong> Permite desenvolver aplicativos mais rápido e com menos bugs. </li>
        </ul><br>

        <h2> Desvantagens </h2>
        <ul>
            <li><strong>Curva de aprendizado:</strong> Pode ser um pouco maior para quem vem de linguagens mais imperativas como Java ou C#. </li>
            <li><strong>Tempo de compilação:</strong> Pode ser um pouco maior do que o de Java, especialmente em projetos grandes ou com muitas anotações. </li>
            <li><strong>Suporte da comunidade:</strong> Ainda é menor do que o de Java ou outras linguagens mais populares. </li>
        </ul><br>

        <p> O contêiner abaixo mostra um exemplo de código feito na linguagem Kotlin. </p>
        <div class="example">
            <p class="code">
                <span class="comp">var</span> <span class="var">num</span> = <span class="num">1</span><br>
                <span class="command">while</span> (<span class="var">num</span> &lt;= <span class="num">10</span>) {<br>
                <span class="indent"><span class="var">num</span>++</span><br>
                <span class="indent"><span class="func">println</span>(<span class="var">num</span>)</span><br>
				}
            </p>
        </div>
    `;
});

markdown.addEventListener("click", () => {
    const content = document.getElementById("languages");
    content.innerHTML = `
        <h1> Markdown </h1>
		<p> Markdown é uma linguagem de marcação leve que permite formatar textos de forma simples e intuitiva. Ela foi criada em 2004 por John Gruber e Aaron Swartz, com o objetivo de facilitar a escrita e a leitura de textos na web. </p>

        <p> Usar Markdown tem várias vantagens, como a facilidade de aprender, a compatibilidade com diversos editores e plataformas, a possibilidade de converter para outros formatos como HTML, PDF e DOCX, e a flexibilidade para personalizar o estilo e o conteúdo. </p>

        <p> As principais funcionalidades do Markdown são: criar títulos, listas, tabelas, blocos de código, links, imagens, citações, ênfases, entre outros. Para isso, basta usar alguns símbolos como asteriscos, cerquilhas, colchetes, parênteses, etc. O Markdown também suporta elementos HTML, caso seja necessário usar alguma tag específica. </p>

        <p> Além disso, o Markdown permite usar extensões que adicionam recursos extras à linguagem, como notas de rodapé, tabelas complexas, fórmulas matemáticas, diagramas, etc. Essas extensões variam de acordo com o editor ou a plataforma que se está usando, mas geralmente seguem um padrão comum. </p>

        <h2> Vantagens / Desvantagens </h2>
        <ul>
            <li><strong>Simplicidade e rapidez na escrita e na leitura de textos.</strong></li>
            <li><strong>Compatibilidade e conversão para diversos formatos e plataformas.</strong></li>
            <li><strong>Flexibilidade e personalização do estilo e do conteúdo.</strong></li>
            <li><strong>Extensibilidade e funcionalidades extras através de extensões.</strong></li>
        </ul><br>

        <p> O contêiner abaixo mostra um exemplo de código feito em Markdown. </p>
        <div class="example">
            <p class="code">
                <span class="title"># Example.md</span><br>
                This is just a example Markdown file.
            </p>
        </div>
    `;
});
