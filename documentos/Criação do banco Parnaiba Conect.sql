create database DB_PC;
use DB_PC;

/*
drop table receita;
drop table despesas;
drop table folha_pagamento;
drop table folha_pagamento_holerite;
*/

create table receita (
Data_receita date, 
Ficha_Receita int, 
Conta_Contabil varchar(20), 
Descricao varchar(200), 
Codigo_DR varchar(15), 
Descricao_DR varchar(200), 
Orcado DECIMAL(10,2),
Lancado DECIMAL(10,2), 
Arrecadado DECIMAL(10,2),
id_execucao int,
FOREIGN KEY (id_execucao) REFERENCES Execucao_carga(id_execucao)
);

create table despesas (
Empenho int, 
Data_Despesa date, 
CPFCNPJ varchar(20), 
CredorFornecedor varchar(50), 
Descricao varchar(350), 
Mod_Lic varchar(25), 
Licitacao varchar(15), 
Empenhado DECIMAL(10,2),
Liquidado DECIMAL(10,2), 
Pago DECIMAL(10,2),
id_execucao int,
FOREIGN KEY (id_execucao) REFERENCES Execucao_carga(id_execucao)
);

create table folha_pagamento(
Nome_funcionario varchar(200),
Data_Admissao	Date,
Departamento	varchar(200),
Cargo_Funcao	varchar(100),
Salario_Base	DECIMAL(10,2),
Sexo varchar(1),
id_execucao int,
FOREIGN KEY (id_execucao) REFERENCES Execucao_carga(id_execucao)
);

create table folha_pagamento_holerite(
Codigo_funcionario int, 
Data_Admissao Date, 
Departamento varchar(200), 
Cargo_Funcao varchar(100), 
Salario_Base DECIMAL(10,2), 
Salario_Bruto DECIMAL(10,2), 
Vlr_Adiant DECIMAL(10,2), 
Vlr_Liquido DECIMAL(10,2),
id_execucao int,
FOREIGN KEY (id_execucao) REFERENCES Execucao_carga(id_execucao)
);

create table Cad_Departamento (
id_departamento int not null auto_increment, 
nm_departamento varchar(200), 
primary key(id_departamento)
);

create table Cad_Cargo (
id_cargo int not null auto_increment, 
nm_cargo varchar(100), 
id_departamento int,
primary key(id_cargo),
FOREIGN KEY (id_departamento) REFERENCES Cad_Departamento(id_departamento)
);

create table Cad_Funcionadio (
id_Funcionario int not null auto_increment, 
nome_funcionario varchar(200),
id_cargo int,
primary key(id_Funcionario),
FOREIGN KEY (id_cargo) REFERENCES Cad_Cargo(id_cargo)
);

create table Execucao_carga (
id_execucao int not null auto_increment, 
tipo_relatorio varchar(50),
data_execucao date,
descricao_execucao varchar(200),
status_execucao char(1),
primary key(id_execucao)
)

