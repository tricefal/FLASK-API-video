$ createdb BDD_Video

BDD_Video=#    // For the rest :
create table video_info (
	id serial,		-- esquivalent to auto_increment in mysql
	title varchar(100),
	views int default 1,
	likes int default 1
);

insert into video_info (title) 
values (
	"Intégral de Cabrel",
	"Comment construire une chaise à bascule",
	"API REST avec Flask"
);
