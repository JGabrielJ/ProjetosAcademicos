let vscode = document.getElementById("vscode");
let webstorm = document.getElementById("webstorm");
let pycharm = document.getElementById("pycharm");
let android = document.getElementById("android");
let online = document.getElementById("online");

vscode.addEventListener("click", () => {
    const content = document.getElementById("tools");
    content.innerHTML = `
        <h1> Visual Studio Code (VSCode) </h1>
        <p> O Visual Studio Code é um editor de código-fonte desenvolvido pela Microsoft, que suporta diversas linguagens de programação e plataformas. Ele é gratuito, de código aberto e possui uma interface simples e intuitiva. </p>

        <p> Uma das razões para usar o Visual Studio Code é a sua extensa biblioteca de extensões, que permitem personalizar e melhorar a experiência de desenvolvimento. Além disso, ele possui recursos integrados de depuração, controle de versão, terminal, formatação de código, refatoração e muito mais. </p>

        <p> Entre as principais funcionalidades do Visual Studio Code, podemos destacar: IntelliSense (um recurso de autocompletar que oferece sugestões inteligentes de código, baseadas no contexto e na sintaxe da linguagem), Live Share (um recurso de colaboração em tempo real que permite compartilhar sessões de codificação com outros desenvolvedores, podendo editar, depurar e testar o código juntos), Remote Development (um recurso que permite acessar e editar o código em ambientes remotos, como contêineres, máquinas virtuais ou servidores SSH) e GitHub Codespaces (um recurso que permite criar e usar espaços de código hospedados no GitHub, que são ambientes de desenvolvimento completos e personalizados). </p>

        <h2> Vantagens </h2>
        <ul>
            <li><strong>É leve, rápido e fácil de usar.</strong></li>
            <li><strong>É compatível com diversas linguagens e plataformas.</strong></li>
            <li><strong>Possui uma grande variedade de extensões e recursos integrados.</strong></li>
            <li><strong>Facilita a colaboração e o desenvolvimento remoto.</strong></li>
        </ul><br>

        <h2> Desvantagens </h2>
        <ul>
            <li><strong>Pode consumir muita memória e CPU em alguns casos.</strong></li>
            <li><strong>Pode apresentar alguns bugs ou inconsistências em algumas extensões ou funcionalidades.</strong></li>
            <li><strong>Pode exigir um tempo de adaptação para quem está acostumado com outros editores.</strong></li>
        </ul><br>

        <p> A imagem abaixo ilustra como é a interface do software Visual Studio Code. </p>
        <img src="./images/tool-icons/print-vscode.png" alt="VSCode Interface" width="700px" height="421px">
    `;
});

webstorm.addEventListener("click", () => {
    const content = document.getElementById("tools");
    content.innerHTML = `
        <h1> WebStorm </h1>
		<p> O WebStorm é um IDE (Integrated Development Environment) para desenvolvimento web, que oferece suporte a diversas linguagens e frameworks, como JavaScript, TypeScript, React, Angular, Vue, Node.js, HTML, CSS e Sass. Ele é desenvolvido pela JetBrains, uma empresa conhecida por criar ferramentas de alta qualidade para programadores. </p>

        <p> Um dos motivos para usar o WebStorm é que ele facilita a escrita de código limpo e eficiente, graças aos seus recursos de edição inteligente, como autocomplete, refatoração, correção de erros, formatação e navegação. Além disso, o WebStorm integra-se com ferramentas externas, como depuradores, testadores, gerenciadores de pacotes e sistemas de controle de versão, permitindo que o desenvolvedor tenha um ambiente completo e produtivo. </p>

        <p> Algumas das principais funcionalidades do WebStorm são: suporte a diversos frameworks e bibliotecas web, como React, Angular, Vue, Express, Jest, Mocha e outros, com templates, snippets e componentes específicos para cada um deles; suporte a TypeScript, um superset de JavaScript que adiciona tipos estáticos e outros recursos ao código. O WebStorm oferece autocomplete, refatoração, verificação de tipos e compilação de TypeScript; suporte a HTML, CSS e Sass, com autocomplete, validação, formatação e pré-processamento de código. O WebStorm também permite visualizar o resultado do código HTML e CSS no navegador ou em um painel integrado; suporte a Node.js, com depuração integrada, execução de scripts, gerenciamento de pacotes npm ou yarn e integração com o Docker e o Kubernetes. </p>

        <h2> Vantagens </h2>
        <ul>
            <li><strong>Oferece um ambiente integrado e rico em recursos para desenvolvimento web.</strong></li>
            <li><strong>Facilita a escrita de código limpo e eficiente com edição inteligente e refatoração.</strong></li>
            <li><strong>Integra-se com diversas ferramentas externas para depuração, teste, controle de versão e implantação.</strong></li>
            <li><strong>Suporta as tecnologias mais recentes e populares do mercado web.</strong></li>
        </ul><br>

        <h2> Desvantagens </h2>
        <ul>
            <li><strong>É um software pago e relativamente caro em comparação com outras opções gratuitas ou mais baratas.</strong></li>
            <li><strong>Pode ser pesado e lento em alguns casos, consumindo muitos recursos do computador.</strong></li>
            <li><strong>Pode ter uma curva de aprendizado alta para quem não está acostumado com a interface e os recursos da JetBrains.</strong></li>
        </ul><br>

        <p> A imagem abaixo ilustra como é a interface do software WebStorm. </p>
        <img src="./images/tool-icons/print-webstorm.png" alt="WebStorm Interface" width="700px" height="421px">
    `;
});

pycharm.addEventListener("click", () => {
    const content = document.getElementById("tools");
    content.innerHTML = `
        <h1> PyCharm </h1>
		<p> PyCharm é uma IDE (Integrated Development Environment) para Python, que oferece um ambiente de desenvolvimento completo e integrado para programadores. PyCharm facilita a escrita, a depuração, o teste e a execução de código Python, além de oferecer recursos avançados de análise de código, refatoração e integração com outras ferramentas. </p>

        <p> PyCharm é uma ótima opção para quem quer desenvolver projetos em Python de forma rápida, eficiente e organizada. PyCharm permite que o programador se concentre na lógica e na criatividade do seu código, sem se preocupar com detalhes técnicos ou burocráticos. PyCharm também ajuda a manter a qualidade e a consistência do código, seguindo as melhores práticas e padrões da linguagem. </p>

        <h2> Vantagens </h2>
        <ul>
            <li><strong>Suporte a diversos frameworks e bibliotecas de Python, como Django, Flask, NumPy, Pandas, TensorFlow, etc.</strong></li>
            <li><strong>Autocompletar inteligente de código, que sugere nomes de variáveis, funções, classes e módulos.</strong></li>
            <li><strong>Depurador gráfico, que permite inspecionar e modificar o estado das variáveis, executar passo a passo o código e definir pontos de interrupção.</strong></li>
            <li><strong>Testador integrado, que permite executar e gerenciar testes unitários, de integração e de desempenho.</strong></li>
            <li><strong>Editor versátil, que permite personalizar o tema, a fonte, a indentação e outros aspectos da interface.</strong></li>
            <li><strong>Ferramentas de refatoração, que permitem renomear, mover, extrair e modificar elementos do código de forma segura e automática.</strong></li>
            <li><strong>Integração com sistemas de controle de versão, como Git, SVN, Mercurial, etc.</strong></li>
        </ul><br>

        <h2> Desvantagens </h2>
        <ul>
            <li><strong>Ser uma ferramenta paga (embora exista uma versão gratuita para estudantes e projetos de código aberto).</strong></li>
            <li><strong>Consumir muitos recursos do computador, podendo ficar lento ou travar em máquinas mais antigas ou com pouca memória.</strong></li>
            <li><strong>Ter uma curva de aprendizado relativamente alta, exigindo que o usuário se familiarize com as diversas opções e configurações da IDE.</strong></li>
        </ul><br>

        <p> A imagem abaixo ilustra como é a interface do software PyCharm. </p>
        <img src="./images/tool-icons/print-pycharm.png" alt="PyCharm Interface" width="700px" height="421px">
    `;
});

android.addEventListener("click", () => {
    const content = document.getElementById("tools");
    content.innerHTML = `
        <h1> Android Studio </h1>
		<p> O Android Studio é uma ferramenta de desenvolvimento integrado (IDE) para criar aplicativos para o sistema operacional Android. Ele é baseado no IntelliJ IDEA, uma IDE popular para Java e outras linguagens de programação. </p>

        <p> O Android Studio oferece várias vantagens para os desenvolvedores de aplicativos Android, tais como: um editor de código inteligente, que fornece recursos como auto-completar, refatorar, depurar e testar; um designer de layout, que permite criar interfaces gráficas de forma visual e interativa; um emulador, que simula o comportamento de um dispositivo Android real no computador; um gerenciador de SDK, que facilita o download e a atualização das versões do Android e das bibliotecas necessárias; e um sistema de build, que automatiza o processo de compilação, empacotamento e distribuição do aplicativo. </p>

        <p> As principais funcionalidades do Android Studio são: a criação de projetos a partir de modelos pré-definidos ou personalizados, que incluem os arquivos e as configurações básicas para o aplicativo; a edição de código-fonte em Java, Kotlin ou C++, com suporte a sintaxe, formatação, navegação e documentação; a depuração e o teste do aplicativo, com ferramentas para inspecionar variáveis, avaliar expressões, definir pontos de interrupção e executar testes unitários e instrumentados; a análise do desempenho do aplicativo, com ferramentas para medir o uso de memória, CPU, rede e bateria, além de identificar gargalos e vazamentos; e a publicação do aplicativo na Google Play Store ou em outros canais de distribuição, com ferramentas para gerar assinaturas digitais, versões de lançamento e relatórios de qualidade. </p>

        <h2> Vantagens </h2>
        <ul>
            <li><strong>Ser gratuita e de código aberto, permitindo que os desenvolvedores contribuam com melhorias e correções.</strong></li>
            <li><strong>Ser compatível com diversos sistemas operacionais, como Windows, Linux e Mac OS.</strong></li>
            <li><strong>Ser integrada com outros serviços e plataformas da Google, como Firebase, Google Maps e Google Cloud.</strong></li>
            <li><strong>Ser atualizada frequentemente com as novidades e as tendências do mercado de aplicativos Android.</strong></li>
        </ul><br>

        <h2> Desvantagens </h2>
        <ul>
            <li><strong>Exigir um computador com boas especificações técnicas, como memória RAM, processador e espaço em disco.</strong></li>
            <li><strong>Apresentar alguns bugs e instabilidades em algumas versões ou funcionalidades.</strong></li>
            <li><strong>Ter uma curva de aprendizado relativamente alta para os iniciantes ou para quem vem de outras IDEs.</strong></li>
        </ul><br>

        <p> A imagem abaixo ilustra como é a interface do software Android Studio. </p>
        <img src="./images/tool-icons/print-android.png" alt="Android Studio Interface" width="700px" height="421px">
    `;
});

online.addEventListener("click", () => {
    const content = document.getElementById("tools");
    content.innerHTML = `
        <h1> Editores de Código Online </h1>
		<p> Editores de código online são ferramentas que permitem criar, editar e executar códigos de diferentes linguagens de programação diretamente no navegador, sem a necessidade de instalar nenhum software adicional no computador. </p>

  		<p> Uma das principais razões para usar editores de código online é a praticidade e a conveniência de poder acessar seus projetos de qualquer lugar e em qualquer dispositivo, desde que tenha uma conexão com a internet. Além disso, os editores de código online oferecem recursos como colaboração em tempo real, integração com serviços de hospedagem e versionamento, e suporte a diversas bibliotecas e frameworks. </p>

  		<p> Algumas das funcionalidades mais comuns dos editores de código online são: autocompletar (sugere palavras-chave, variáveis e funções conforme o usuário digita, facilitando a escrita do código e evitando erros de sintaxe), destaque de sintaxe (colore o código de acordo com as regras da linguagem escolhida, melhorando a legibilidade e a organização do código), depuração (permite testar e corrigir o código em tempo real, identificando possíveis falhas e bugs) e formatação (ajusta o espaçamento, a indentação e o alinhamento do código, seguindo padrões estabelecidos ou personalizados pelo usuário). </p>

        <p> Existem vários sites que também cumprem a mesma função de uma IDE comum, alguns com uma função mais didática e educativa, com funcionalidades reduzidas (claro), utilizando até mesmo programação em blocos, e outros que são simuladores virtuais. Alguns editores didáticos conhecidos são <a href="https://code.org/" target="_blank">Code.org</a>, <a href="https://developers.google.com/blockly?hl=pt-br" target="_blank">Blockly</a>, <a href="https://www.w3schools.com/tryit/" target="_blank">W3Schools</a> e <a href="https://www.tinkercad.com/dashboard" target="_blank">Tinkercad</a> (ao criar projetos com Arduíno, é necessário programá-lo para que funcione corretamente). Os simuladores virtuais mais populares são <a href="https://codepen.io/" target="_blank">Codepen</a>, <a href="https://replit.com/" target="_blank">Replit</a>, <a href="https://vscode.dev/" target="_blank">VSCode Dev</a> e <a href="https://www.gitpod.io/" target="_blank">Gitpod</a>.</p>

  		<h2> Vantagens </h2>
        <ul>
            <li><strong>Não requer instalação nem configuração prévia.</strong></li>
            <li><strong>Permite trabalhar em diferentes plataformas e sistemas operacionais.</strong></li>
            <li><strong>Facilita o compartilhamento e a colaboração entre desenvolvedores.</strong></li>
            <li><strong>Mantém os arquivos salvos na nuvem, evitando perdas ou danos.</strong></li>
        </ul><br>

        <h2> Desvantagens </h2>
        <ul>
            <li><strong>Depende da disponibilidade e da velocidade da internet.</strong></li>
            <li><strong>Pode ter limitações de recursos ou compatibilidade com algumas linguagens ou bibliotecas.</strong></li>
            <li><strong>Pode comprometer a segurança e a privacidade dos dados armazenados online.</strong></li>
        </ul><br>

        <p> A imagem abaixo ilustra como é a interface do software Replit. </p>
        <img src="./images/tool-icons/print-replit.svg" alt="Replit Interface" width="700px" height="421px">
    `;
});
