/*
The purpose of this file is to show a sample of my SAS techniques and abilities.
This file is currently being updated.
The dataset used here is available in all SAS platforms.
*/


/*XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX*/
/*
The following lines show usage of:
	-data step
	-proc sql
	-proc print
	-ods
*/


data heartdata;
	set sashelp.heart
		(rename=(DeathCause=CauseOfDeath)
			keep=Status DeathCause AgeCHDdiag AgeAtStart Height Weight);
	if AgeAtStart > 30 and AgeAtStart < 50;
run;


proc sql;
create table heartdata2 as
	(
	select Status 
		, AgeAtStart 
		, avg(AgeCHDdiag) as AverageAgeCHDdiag  
		, avg(Height) as AverageHeight    
		, avg(Weight) as AverageWeight
	from heartdata
	group by Status, AgeAtStart
	)
	order by Status, AgeAtStart
	;
quit;


ods excel file="/folders/myfolders/HeartStudy.xlsx" 
options
	(
	start_at="3,3"
	frozen_headers="5"
	frozen_rowheaders="3"
	sheet_name="Heart_Study"
	embedded_titles="yes"
	);
 
proc print data=heartdata2; 
title "Average Height, Weight, and AgeCHDdiag by Status and Age";
run;
 
ods excel close;

/*XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX*/
/*
The following lines show usage of:
	-global macros
	-local macros
*/


%LET main_dataset = sashelp.heart;
%LET output_destination = "/folders/myfolders/HeartStudy2.xlsx";


%MACRO printexcel;
	data datasubset;
		set &main_dataset;
	run;

	ods excel file=&output_destination
	options
		(
		start_at="3,3"
		frozen_headers="5"
		frozen_rowheaders="3"
		sheet_name= &main_dataset
		embedded_titles="yes"
		);

	proc print data=datasubset;
	run;

	ods excel close;

%MEND printexcel;


%printexcel


