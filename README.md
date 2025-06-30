## Padrão Singleton

### O que é?

O padrão Singleton garante que uma classe tenha apenas uma instância e fornece um ponto de acesso global a essa instância.

### Quando usar?
- Quando deve existir somente um objeto controlando um recurso.
- Ex: gerenciadores de configuração, conexão com banco de dados, logger.

### Pontos Fortes
- Garante uma única instância.

- Evita acesso concorrente indesejado em ambientes multi-thread.

- Útil para recursos globais (ex: logger, banco de dados).

### Pontos Fracos
- Pode dificultar testes (ex: testes unitários com dependências globais).

- Viola o princípio da responsabilidade única.

- Pode introduzir estado global acoplado à aplicação.

### Variações do Singleton
# Singleton preguiçoso (lazy instantiation)
- A instância só é criada quando for usada pela primeira vez.
- Menor uso de memória, porém pode ter problemas em ambiente concorrente.

# Singleton ávido (eager instantiation)
- A instância é criada logo na inicialização do programa.
- Mais seguro, porém consome memória mesmo se não for usada.

# Thread-safe Singleton
- Adiciona travas (locks) para garantir segurança em sistemas multi-thread.

### Vantagens
# Vantagem	              Descrição
- Acesso global	          Permite acessar a instância de qualquer lugar.
- Controle de instância	  Garante que só exista uma instância viva.
- Economia de recursos	  Útil quando a criação de objetos é cara (Ex: conexão BD).
- Fácil integração	      Pode ser integrado com outros padrões (ex: Singleton + Factory).

### Desvantagens
# Problema	              Explicação
- Atrapalha testes	      Pode criar dependência global e dificultar testes unitários.
- Viola SRP	              Responsável por criar a instância e armazenar estado global.
- Pode gerar concorrência	Em ambientes com múltiplas threads, pode criar múltiplas instâncias sem proteção.
- Dificulta manutenção	  Mudanças no Singleton impactam várias partes do sistema.

### Boas Práticas
- Use Singleton apenas quando necessário.
- Combine com injeção de dependência para facilitar testes.
- Se estiver em ambiente com múltiplas threads, sempre use uma versão thread-safe.
- Mantenha o estado interno do Singleton imutável sempre que possível.

### Situações onde NÃO usar
- Quando o objeto pode ser criado várias vezes sem custo.
- Quando a classe precisa de mais de uma instância (como configurações diferentes).
- Quando o código precisa ser altamente testável e desacoplado.
- Quando você pode usar injeção de dependência no lugar.

## Padrão Factory Method

### O que é?
O Factory Method define uma interface para criar objetos, mas permite que subclasses decidam qual classe instanciar. Ele delega a responsabilidade da criação para subclasses, promovendo flexibilidade e reutilização de código.

### Quando usar?
- Quando o código precisa trabalhar com objetos cujas classes exatas só são conhecidas em tempo de execução.
- Quando se deseja desacoplar a criação de objetos do seu uso.

### Pontos Fortes
- Desacopla a criação de objetos do código cliente.

- Facilita a adição de novos tipos de produtos.

- Segue o princípio aberto/fechado (OCP) e o princípio da responsabilidade única (SRP).

### Pontos Fracos
- Aumenta a complexidade com mais classes.

- Pode ser excessivo para casos simples.

### Variações do Factory Method
# Factory Method Puro (Clássico – GoF)
- É o padrão original descrito no livro da Gang of Four, em que:
- Existe uma superclasse (ou interface abstrata) com um método criarProduto(), que é sobrescrito pelas subclasses concretas.

# Factory Method com Parâmetros
- Permite que o método de fábrica receba argumentos e, com base neles, decida qual objeto retornar.

# Factory Method Estático
- O método criar() é estático (usado sem precisar instanciar a fábrica). Muito comum em linguagens como Java, C# e Python.

### Vantagens
# Vantagem	                  Explicação
- Desacoplamento	            O código cliente não precisa saber qual classe concreta está sendo instanciada, apenas usa a interface. Isso facilita a manutenção e a substituição de implementações.
- Aberto para extensão	      É fácil adicionar novos produtos sem modificar o código existente (Princípio Aberto/Fechado - OCP). Basta criar uma nova subclasse que implemente o método fábrica.
- Maior flexibilidade	        Permite que subclasses decidam qual objeto criar, tornando o sistema mais adaptável a mudanças e diferentes contextos.
- Facilita testes	            Como as dependências são abstraídas, é mais fácil usar objetos falsos (mocks) em testes.
- Organização do código	      Centraliza a lógica de criação de objetos, evitando duplicação de código de instanciamento.
- Boa base para frameworks	  É amplamente utilizado em frameworks e bibliotecas que precisam criar objetos de forma genérica e reutilizável.

### Desvantagens
# Desvantagem	                                  Explicação
- Mais classes e complexidade	                  Requer a criação de interfaces/abstrações e múltiplas subclasses, o que pode aumentar a complexidade e a quantidade de arquivos.
- Pode ser desnecessário em casos simples	      Para projetos pequenos ou com poucos objetos, o uso do Factory Method pode ser um exagero.
- Curva de aprendizado	                        Para iniciantes, pode ser confuso entender a separação entre fábrica, produto e cliente.
- Pode violar o (SRP)	                          Se a fábrica tiver muita lógica interna, ela pode assumir mais responsabilidades do que deveria.
- Não evita dependências se mal implementado    Se o método fábrica for mal feito (ex: com if ou switch em vez de polimorfismo), ainda haverá acoplamento com classes concretas.

### Boas Práticas
- Crie uma hierarquia de produtos base (ex: Transporte, Animal, Inimigo) para garantir que todas as classes concretas compartilhem um contrato comum.
- Use nomes claros como criarTransporte(), fabricarProduto() ou obterInstancia() para indicar que a função é responsável pela criação.
- Evite muitos if ou switch dentro da fábrica, prefira usar polimorfismo ou registro de classes (ex: dicionários) para tornar o código mais extensível e limpo.

### Situações onde NÃO usar
- Quando o sistema precisa de desempenho máximo, o uso de abstrações pode impactar levemente o desempenho, especialmente em sistemas embarcados ou críticos em tempo real.
- Quando os objetos precisam de muitos parâmetros complexos para criação, neste caso, o padrão Builder pode ser mais indicado do que Factory Method.
- Quando há apenas uma ou duas classes concretas fixas, o overhead de criar fábricas, interfaces e subclasses pode ser desnecessário para algo simples.

### Conclusão
- Singleton é útil quando há necessidade de compartilhar uma única instância no sistema, mas seu uso deve ser moderado para evitar problemas de acoplamento e testabilidade.

- Factory Method promove um design mais limpo e flexível, ideal para aplicações que crescem e precisam instanciar diversos tipos de objetos sem modificar o código cliente.

- Ambos os padrões resolvem problemas diferentes, e sua escolha deve ser feita com base nos requisitos do projeto e no contexto de uso.

- Em conjunto, eles podem até ser usados no mesmo sistema: o Singleton para garantir uma única instância da fábrica, e o Factory Method para criar objetos dentro dela.