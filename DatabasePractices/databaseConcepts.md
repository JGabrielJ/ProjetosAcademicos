# Definições sobre Bancos de Dados

- Dado: os dados são um meio necessário para a compreensão e/ou entendimento de uma determinada coisa,
como o produto de uma loja. Eles são o que nós conhecemos como as características de um determinado objeto.

- Informação: é aquilo que compõe o arquivo de uma determinada função ou área de um setor, sendo ele de uma
empresa ou não.

- Arquivo Convencional: é o responsável por armazenar um conjunto de informações, que por sua vez é formado de variados
outros conjuntos de dados.

- Banco de Dados: este, por sua vez, é o conjunto de dados integrados cujo objetivo é atender a uma comunidade de
usuários ou, de forma resumida, é um conjunto de arquivos convencionais integrados entre si.

- Sistema Isolado: nos sistemas isolados, os dados não são compartilhados entre si, tendo cada sistema o seu próprio
arquivo convencional, com cada dado e informação guardados separadamente dos outros sistemas. Um exemplo disso é o
funcionamento de uma empresa, onde existem três setores: produção, vendas e compras. Cada setor tem o seu próprio
arquivo (um arquivo da produção, outro das vendas e outro das compras), onde neles estão armazenados os dados e
informações de cada produto dessa empresa. Os problemas desse tipo de sistema são a redundância controlada de dados
(onde o software a gerencia) e a não controlada (onde o usuário a gerencia). A redundância não controlada de dados
pode causar inconsistência de dados e a entrada repetida da mesma informação.

- Sistema Integrado: como forma de solucionar o problema da redundância não controlada de dados, os sistemas integrados
vêm com o objetivo de proporcionar o compartilhamento de dados, onde cada informação é armazenada uma única vez e, ao
invés das informações estarem guardadas em vários arquivos separados, é utilizado um banco de dados para armazenar todas
essas informações. Um banco de dados nada mais é que, de forma resumida, um conjunto de arquivos convencionais que armazenam
dados. Utilizando o exemplo anterior, cada setor estará conectado a um único banco de dados que está armazenando todos os
dados e informações dos produtos da empresa. A implementação desse tipo de sistema resulta em algumas consequências, como
a estrutura interna dos arquivos passar a ser mais complexa e ter a necessidade de atender às necessidades de diferentes setores.

- Modelagem Conceitual: o modelo conceitual é uma descrição do banco de dados que não depende do tipo de Sistema de
Gerência de Banco de Dados (SGBD) e faz o registro da estrutura dos dados que podem aparecer no banco de dados. O que
esse modelo não registra é como esses dados vão estar armazenados quando chegar o momento de implementar a aplicação
em um SGBD. O modelo conceitual é representado através de um DER (Diagrama Entidade-Relacionamento), que por sua vez
faz uso da abordagem entidade-relacionamento (ER), a técnica mais difundida de modelagem conceitual. Utilizando novamente
o exemplo da empresa, um modelo de DER pode informar, por exemplo, que o banco de dados contém dados a respeito de produtos
e sobre os tipos de produtos. Para cada produto, o banco de dados registra seu código, sua descrição e seu preço, bem como
o tipo de produto ao qual o mesmo está associado. Para cada tipo de produto, o banco de dados armazena seu código e sua
descrição, assim como os produtos pertencentes àquele tipo.

- Projeto Lógico: o modelo lógico é uma descrição do banco de dados no nível de abstração que pode ser visualizado
pelo usuário do SGBD e, diferente do modelo conceitual, este depende do tipo de SGBD que está sendo utilizado. Em
um SGBD relacional, os dados estão organizados em forma de tabelas. Ele deve definir quais as tabelas que o banco
contém e, para cada tabela, quais os nomes das colunas.

- Projeto Físico: o modelo físico contém detalhes de armazenamento interno de informações, detalhes estes que não
têm influência sobre a programação de aplicações no SGBD, mas que influenciam no desempenho das aplicações. Estes
tipos de modelo são usados apenas por profissionais que fazem sintonia (ajuste de desempenho ou "tuning") de banco
de dados. Esse processo é adequado para a construção de um novo banco de dados, mas caso já exista um banco de dados
ou um conjunto de arquivos convencionais, e pretende-se construir um novo banco de dados, o processo é modificado e
incorpora uma etapa de engenharia reversa.

- Entidade: é um conjunto de objetos da realidade modelada sobre os quais deseja-se manter informações no
banco de dados. Ela pode representar objetos concretos da realidade (como uma pessoa, um automóvel etc.)
ou objetos abstratos (como um departamento, um endereço, dentre outros). Em um diagrama ER, ela é representada
através de um retângulo. Quando deseja-se referir um objeto em particular, são utilizadas nomenclaturas
específicas, como instância ou ocorrência de entidade. Se uma entidade estiver isolada, ela possuirá poucas
informações e será necessário atribuir propriedades à elas.

- Relacionamento: é um conjunto de associações entre entidades (ou instâncias de entidades) sobre as quais deseja-se
manter informações na base de dados. Em um diagrama ER, ela é representada através de um losango que conecta duas
entidades (retângulos) entre si. Em um auto-relacionamento, apenas uma entidade (retângulo) está conectada ao
relacionamento (losango), às vezes desempenhando um papel de entidade, que é uma função que uma ocorrência de
uma entidade cumpre em uma ocorrência de um relacionamento. Em relacionamentos entre entidades diferentes não
é usual indicar os papéis das entidades. Um relacionamento binário é aquele cujas instâncias envolvem duas
instâncias de entidades. Existem três tipos de relacionamento binário, que são o n:n (muitos-para-muitos),
o 1:n (um-para-muitos) ou o n:1 (muitos-para-um) e o 1:1 (um-para-um). Existem também relacionamentos ternários,
onde três entidades estão sendo interligadas por um único relacionamento.

- Atributo: é um dado ou informação que é associado a cada ocorrência de uma entidade ou de um relacionamento.
Em um diagrama ER, ele é representado através de círculos que ficam conectados às suas respectivas entidades
(retângulos). Assim como entidades, relacionamentos também podem possuir atributos.

- Domínio de um Atributo: é o conjunto de valores que um determinado atributo (representado por círculos em um diagrama
entidade-relacionamento) pode assumir.

- Generalização / Especialização: este conceito permite atribuir propriedades particulares a um subconjunto das ocorrências
(especializadas) de uma entidade genérica. Em um diagrama ER, ela é representada através de triângulos que interligam dois
tipos de entidades (retângulos): a entidade genérica e a entidade especializada, que herda as propriedades da entidade genérica.
A árvore de herança deve ter uma única entidade que define o identificador, ou seja, a herança de múltiplos identificadores
é um caso proibido. Em uma especialização total, é indicado que toda entidade genérica é obrigatoriamente uma de suas duas
entidades especializadas, representado através da letra t. Em uma especialização parcial, é indicado que nem toda entidade
genérica é obrigatoriamente uma de suas duas entidades especializadas, representado através da letra p. Em uma especialização
não exclusiva ou compartilhada, é indicado que uma instância de entidade genérica pode aparecer em mais de uma de suas entidades
especializadas, representado através do c.

- Entidade Associativa: entidades associativas modificam um pouco o modelo tradicional de ER. Em um exemplo onde duas
entidades (MÉDICO e PACIENTE) estão interligadas atarvés de um relacionamento n:n (CONSULTA), precisamos adicionar a
informação de que medicamentos foram prescritos em uma consulta. Para isso, substituímos um relacionamento por uma
entidade, estabelecendo um relacionamento 1:n entre [MÉDICO e CONSULTA] e [PACIENTE e CONSULTA]. Após isso, estabelecemos
um relacionamento n:n (PRESCRIÇÃO) entre [CONSULTA e MEDICAMENTO]. Neste caso, o relacionamento CONSULTA se transformaria
em uma entidade associativa (losango dentro de retângulo, em um DER).

- Cardinalidade de um Atributo: ela define quantos valores de um atributo podem estar associados a uma ocorrência da entidade
ou relacionamento a qual ele pertence. A representação diagramática da cardinalidade de atributos é derivada da representação
da cardinalidade de entidades em relacionamentos. No caso de a cardinalidade ser (1,1) ela pode ser omitida do diagrama. Assim,
atributos obrigatórios são de cardinalidade mínima 1, ou seja, cada entidade possui no mínimo um valor associado e atributos
monovalorados são de cardinalidade máxima 1, isto é, cada entidade possui no máximo um valor associado. No caso de atributos
opcionais, eles possuem cardinalidade mínima 0 e atributos multivalorados possuem cardinalidade máxima n.