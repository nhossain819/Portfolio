--DESCRIPTION:
--The purpose of this file is to show a sample of my SQL techniques and abilities.

--These queries are based on queries I wrote while in previous positions.

--To respect confidentiality, the code below does not contain any database, table, or column name used in any of my previous positions.

--These tasks and queries below involve a hypothetical company that delivers cakes and pies to individuals in offices internationally.

--The schema of the hypothetical company database is available upon request.


--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
--TASK 1
--Create a single table that contains:
--  	The account_id_number and name of every active account in region 3 of Italy.
--  	The numbers of cake and pie customers for each company account.
--  	The count of active individuals listed for each company account.
--  	The count of individuals who ordered at least one cake or pie between 7/12/2016 and 2/25/2018.


--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
--QUERY FOR TASK 1
SELECT *

FROM
			(SELECT dc.account_id_number
				, dc.company_name
				, dc.total_cake_orders
				, dc.total_pie_orders
				, count(distinct(di.individual_id) as Num_Act_Individuals

			FROM dimension_company as dc

			LEFT JOIN dimension_individual as di
				on di.account_id=dc.id

			WHERE dc.region_id ='italy3'
				and dc.active = '1'

			GROUP BY dc.account_id_number
				, dc.company_name
				, dc.total_cake_orders
				, dc.total_pie_orders

			ORDER BY dc.account_id_number
			)
		as main_query

LEFT JOIN
			(SELECT dc.account_id_number
					,count(distinct(di.individual_id)) as Num_Cakes_Delivered

			FROM fact_individual_cake_delivered as ficd

			INNER JOIN dimension_individual as ds
				on ficd.individual_id = di.individual_id

			INNER JOIN dimension_company as da
				on di.account_id=dc.id

			WHERE
				ficd.status = '2'
				and (ficd.delivery_time > '2016-07-12 00:00:00'
					and ficd.delivery_time < '2018-02-25 23:59:59')

			GROUP BY dc.account_id_number
			)
		as subquery_C
		on main_query.account_id_number = subquery_C.account_id_number

LEFT JOIN
			(SELECT dc.account_id_number
					, count(distinct(di.individual_id)) as count_pies_delivered

			FROM fact_individual_pie_delivered as fipd

			INNER JOIN dimension_individual as ds
				on fipd.individual_id = di.individual_id

			INNER JOIN dimension_company as da
				on di.account_id=dc.id

			WHERE
				fipd.status = '2'
				and (fipd.delivery_time > '2016-07-12 00:00:00'
					and fipd.delivery_time < '2018-02-25 23:59:59')

			GROUP BY dc.account_id_number
			)
		as subquery_P
		on main_query.account_id_number = subquery_P.account_id_number



--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
--TASK 2
--Create a single table containing:
--	The account ID number and Company Name of every active account in region 3 of Italy.
--	The count of active individuals listed in the database by office size and account.
--	The count of individuals who were delivered at least one cake or pie between 7/1/2016 and 2/10/2017 by account and office size.
--	The average number of deliveries in the same time period per individual with at least one order in that time period, by
--		pastry, company, and office size.


--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
--QUERY FOR TASK 2

SELECT aid_s1 as acc_id_number
		, office_size as Office_Size
		, count as Num_of_Active_Individuals
		, num_individuals_with_cake_delivered as Num_Individuals_with_Cake_Delivered
		, num_individuals_with_pie_delivered as Num_Individuals_with_Pie_Delivered
		, avg as AvgNum_of_deliveries_per_ind

FROM
--SECTION ONE
--This first section addresses:
--	The account ID number and Company Name of every active account in region 3 of Italy.
--	The count of active individuals listed in the database by office size and account.

		(
            SELECT dc.acc_id_number as aid_s1
                , dc.company_name
                , di.office_size
                , count(
			    case
	                        when di.active='1'
	                            then di.id
	                                else null
	                                    end
                        ) as count_of_active_id

            FROM dimension_company as dc

            INNER JOIN dimension_individual as di
                on di.acc_id=dc.id

            WHERE dc.region_id = 'italy3'
                and dc.active = '1'

            GROUP BY dc.acc_id_number
                , dc.company_name
                , di.office_size

            ORDER BY aid_s1
        )
        as QUERY1

LEFT JOIN
--SECTION TWO
--This section addresses:
--	The count of individuals who were delivered at least one cake or pie between 7/1/2016 and 2/10/2017 by account and office size.

		(
	            (
					SELECT dc.acc_id_number as aid_s2
					, dc.company_name

				FROM dimension_individual as di

				INNER JOIN dimension_company as dc
					on di.acc_id=dc.id

				WHERE dc.region_id = 'italy3'
					and dc.active = '1'

				GROUP BY dc.acc_id_number
					, dc.company_name

				ORDER BY aid_s2
			)
	    		as main_query

	    		LEFT JOIN

	    		(
				SELECT dc.acc_id_number
		    		, count(distinct(di.individual_id)) as num_individuals_with_cake_delivered

		    		FROM fact_individual_cake_delivered as ficd

		    		INNER JOIN dimension_individual as di
		    		on ficd.individual_id = di.individual_id

		    		INNER JOIN dimension_company as dc
		    		on di.acc_id=dc.id

		    		WHERE
		    		ficd.status = '2'
		    		and (ficd.order_time > '2016-07-01 00:00:00'
		    		and ficd.delivery_time < '2017-02-10 23:59:59')

		    		GROUP BY dc.acc_id_number
	    		)
	    		as subquery_C
	    		on main_query.aid_s2 = subquery_C.acc_id_number

			LEFT JOIN

	    		(
				SELECT dc.acc_id_number
		    		, count(distinct(di.individual_id)) as num_individuals_with_pie_delivered

		    		FROM fact_individual_pie_delivered as fipd

		    		INNER JOIN dimension_individual as di
		    		on fipd.individual_id = di.individual_id

		    		INNER JOIN dimension_company as dc
		    		on di.acc_id=dc.id

		    		WHERE
		    		fipd.status = '2'
		    		and (fipd.order_time > '2016-07-01 00:00:00'
		    		and fipd.delivery_time < '2017-02-10 23:59:59')


		    		GROUP BY dc.acc_id_number
	    		)
				as subquery_E
				on main_query.aid_s2 = subquery_E.acc_id_number
			)
    		as QUERY2
    		on QUERY1.aid_s1 = QUERY2.aid_s2

LEFT JOIN
--SECTION THREE
--This section address:
--	The average number of deliveries in the same time period per individual with at least one cake order in that time period, by
--		company and office size.

	       (
		    	SELECT acc_id_number as aid_s3
	                , avg(deliveries)


	            FROM
					(

	                SELECT dc.acc_id_number
	                    , ficd.individual_id
	                    , count(*) as deliveries

	                FROM fact_individual_cake_delivered as ficd

	                INNER JOIN dimension_individual as di
	                    on di.id = ficd.individual_id

	                INNER JOIN dimension_company as dc
	                    on dc.id = di.acc_id

	            	WHERE
	            	    ficd.status = '2'
		    		and (ficd.order_time > '2016-07-01 00:00:00'
		    		and ficd.delivery_time < '2017-02-10 23:59:59')

	            	GROUP BY dc.acc_id_number
	            	        , ficd.individual_id

	            	)
					as myquery

	            WHERE upper(acc_id_number) like 'ITALY3%'

	            GROUP BY acc_id_number
            )
            as QUERY3
            on QUERY1.aid_s1 = QUERY3.aid_s3




ORDER BY aid_s1
		, office_size



--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
--TASK 3
--Create a single table containing:
--      The account ID number and company name for the top 5 largest accounts in each region by total of individuals per company.
--      The count of individuals listed by account.
--      The count of individuals who ordered atleast one cake or pie between 7/1/2016 and 2/10/2017 by account and baked good.
--      The count of individuals who ordered atleast one cake or pie between 7/12/2016 and 2/25/2018 by account and baked good.


--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
--QUERY FOR TASK 3

SELECT *
FROM
--QUERY1 shows the account ID number and company name for the top 5 largest accounts in each region by total of individuals per company.

        (SELECT subquery.region_id
            , subquery.acc_id_number
            , subquery.company_name
        	, subquery.total_individuals_at_company

        FROM
        	(
        		SELECT dc.region_id
        		    , dc.acc_id_number
        		    , dc.company_name
        			, (dc.total_cake_orders + dc.total_pie_orders) as total_individuals_at_company
        		    , row_number() over(partition by dc.region_id order by (total_individuals_at_company) desc) as rn
        		FROM dimension_company as dc
        		WHERE dc.total_cake_orders > 0
        			and dc.total_pie_orders > 0
        		GROUP BY dc.region_id
        		    , dc.acc_id_number
        		    , dc.company_name
        			, dc.total_cake_orders
        			, dc.total_pie_orders
        	) as subquery
        		WHERE subquery.rn <= 5
        ORDER BY region_id
            ) as QUERY1


LEFT JOIN
--QUERY2 shows the count of individuals listed by account.

        (SELECT dc.acc_id_number
        	, count(*) number_of_active_individuals

        FROM dimension_company as dc

        INNER JOIN dimension_individual as di
            on dc.id=di.acc_id
			and di.active = '1'

        GROUP BY dc.acc_id_number

        ORDER BY dc.acc_id_number
        ) as QUERY2
            on QUERY1.acc_id_number=QUERY2.acc_id_number


LEFT JOIN
--QUERY3 shows the count of individuals who ordered atleast one cake between 7/1/2016 and 2/10/2017 by account.

		(SELECT dc.acc_id_number
				,count(distinct(di.individual_id)) as Number_of_Individuals_with_Cakes_Delivered

		from fact_individual_cake_delivered as ficd

		INNER JOIN dimension_individual as di
			on ficd.individual_id = di.individual_id
            and ficd.status = '2'
			and (ficd.order_time >= '2016-07-01 00:00:00'
				and ficd.delivery_time <= '2017-02-10 23:59:59')

		INNER JOIN dimension_company as dc
        				on di.acc_id=dc.id

		GROUP BY
				dc.id
				, dc.acc_id_number
			)
		as QUERY3
		on QUERY1.acc_id_number = QUERY3.acc_id_number

LEFT JOIN
--QUERY4 shows the count of individuals who ordered atleast one pie between 7/1/2016 and 2/10/2017 by account.
			(SELECT dc.acc_id_number
					, count(distinct(di.individual_id)) as Number_of_Individuals_with_Pies_Delivered

			from fact_individual_pie_delivered as fipd

			INNER JOIN dimension_individual as di
				on fipd.individual_id = di.individual_id
                and fipd.status = '2'
				and (fipd.order_time >= '2016-07-01 00:00:00'
					and fipd.delivery_time <= '2017-02-10 23:59:59')

			INNER JOIN dimension_company as dc
				on di.acc_id=dc.id

			GROUP BY
				dc.id
				, dc.acc_id_number
			)
		as QUERY4
		on QUERY1.acc_id_number = QUERY4.acc_id_number
LEFT JOIN
--QUERY5 shows the count of individuals who ordered atleast one cake between 7/12/2016 and 2/25/2018 by account.
		(SELECT dc.acc_id_number
				,count(distinct(di.individual_id)) as Number_of_Individuals_with_Cakes_Delivered2

		from fact_individual_cake_delivered as ficd

		INNER JOIN dimension_individual as di
			on ficd.individual_id = di.individual_id
            		and ficd.status = '2'
			and (ficd.delivery_time >= '2016-07-12 00:00:00'
				and ficd.delivery_time <= '2018-02-25 23:59:59')

		INNER JOIN dimension_company as dc
        				on di.acc_id=dc.id

		GROUP BY
				dc.id
				, dc.acc_id_number
			)
		as QUERY5
		on QUERY1.acc_id_number = QUERY5.acc_id_number

LEFT JOIN
--QUERY6 shows the count of individuals who ordered atleast one pie between 7/12/2016 and 2/25/2018 by account.
			(SELECT dc.acc_id_number
					, count(distinct(di.individual_id)) as Number_of_Individuals_with_Pies_Delivered2

			from fact_individual_pie_delivered as fipd

			INNER JOIN dimension_individual as di
				on fipd.individual_id = di.individual_id
                	and fipd.status = '2'
			and (fipd.delivery_time >= '2016-07-12 00:00:00'
				and fipd.delivery_time <= '2018-02-25 23:59:59')

			INNER JOIN dimension_company as dc
				on di.acc_id=dc.id

			GROUP BY
				dc.id
				, dc.acc_id_number
			)
		as QUERY6
		on QUERY1.acc_id_number = QUERY6.acc_id_number

ORDER BY QUERY1.region_id
		, QUERY1.total_individuals_at_company desc


--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
--TASK 4
--Create a single table containing:
--      The account_id_number and company_name for all accounts in Germany.
--      The count of cakes and pies delivered between 2/10/2018 and 5/15/2018.
--      The minimum and maxiumum office sizes of individuals having baked goods delivered.


--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
--QUERY FOR TASK 4
SELECT *
FROM
--QUERY1 shows The account ID number and company name for all accounts in Germany.
        (SELECT dc.acc_id_number
            , dc.company_name as account_company_name

        FROM dimension_company as dc

        WHERE dc.region_id = 'Germany'
            ) as QUERY1


LEFT JOIN
--QUERY2 The total numbers of cakes delivered between 2/10/2018 and 5/15/2018 and min and max office size.
        (SELECT dc.acc_id_number
            , count(*) as Num_Cakes_Delivered
            , min(di.office_size) as cake_Office_Size_min
            , max(di.office_size) as cake_Office_Size_max

        FROM fact_individual_cake_delivered as ficd

        INNER JOIN dimension_individual as di
            on ficd.individual_id = di.id
            and ficd.status = 2
            and (ficd.delivery_time >= '2018-02-10 00:00:00'
                and ficd.delivery_time <= '2018-05-15 23:59:59')

        INNER JOIN dimension_company as dc
            on dc.id=di.acc_id
            and dc.region_id = 'Germany'

        GROUP BY dc.acc_id_number
        ) as QUERY2
            on QUERY1.acc_id_number=QUERY2.acc_id_number


LEFT JOIN
--QUERY3 The total numbers of pie deliveries taken between 2/10/2018 and 5/15/2018 and min and max office size.
		(SELECT dc.acc_id_number
            , count(*) as Num_Pies_Delivered
            , min(di.office_size) as Pie_Office_Size_min
            , max(di.office_size) as Pie_Office_Size_max

        FROM fact_individual_pie_delivered as fipd

        INNER JOIN dimension_individual as di
            on fipd.order_year_id = di.id
            and fipd.status = 2
			and (fipd.delivery_time >= '2018-02-10 00:00:00'
            	and fipd.delivery_time <= '2018-05-15 23:59:59')

        INNER JOIN dimension_company as dc
            on dc.id=di.acc_id
            and dc.region_id = 'Germany'

        GROUP BY dc.acc_id_number
			)
		as QUERY3
		on QUERY1.acc_id_number = QUERY3.acc_id_number


--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
--TASK 5
--Create a single table containing:
--      The account ID number and company name for all accounts with individuals who had deliveries in a year later than their order year.
--      Account type for each such company
--      Number of individuals having deliveries in years later than their order year.
--      Number of deliveries associated with previous rules.


--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
--QUERY FOR TASK 5
SELECT *
FROM
--QUERY1 The account ID number and company name for all accounts with individuals who had deliveries in a year later
--	than their order year.
        (SELECT dc.acc_id_number
        	, dc.company_name

        FROM fact_individual_cake_delivered as ficd
		INNER JOIN fact_individual_pie_delivered as fipd
			on ficd.order_year_id=fipd.order_year_id
            and (substring(ficd.order_year, 10, 4) < extract(year from ficd.delivery_time)
            	or substring(fipd.order_year, 10, 4) < extract(year from fipd.delivery_time))
		INNER JOIN dimension_individual as di
            on ficd.order_year_id=di.id
		INNER JOIN dimension_company as dc
            on dc.id = di.acc_id
			and dc.active='1'

		GROUP BY dc.acc_id_number
        	, dc.company_name
        ) as QUERY1

LEFT JOIN
--QUERY2 Account type for each such company.
		(SELECT dc.acc_id_number
        	, dc.account_type
			, dc.current_order_year

        FROM dimension_company as dc

		GROUP BY dc.acc_id_number
        	, dc.account_type
			, dc.current_order_year
		) as QUERY2
			on QUERY1.acc_id_number=QUERY2.acc_id_number



LEFT JOIN
--QUERY3 Number of individuals having deliveries in years later than their order year. (CAKE)
        (SELECT dc.acc_id_number
            , count(distinct(ficd.individual_id)) as num_individuals_with_cake_delivered

        FROM fact_individual_cake_delivered as ficd

        INNER JOIN dimension_individual as di
            on di.id=ficd.order_year_id

        INNER JOIN dimension_company as dc
            on dc.id=di.acc_id

        WHERE cast(substring(ficd.order_year, 10, 4) as int) < extract(year from ficd.delivery_time)

		GROUP BY dc.acc_id_number
        ) as QUERY3
            on QUERY1.acc_id_number=QUERY3.acc_id_number

LEFT JOIN
--QUERY4 Number of individuals having deliveries in years later than their order year. (PIE)
        (SELECT dc.acc_id_number
            ,  count(distinct(fipd.individual_id)) as num_individuals_with_pie_delivered

        FROM fact_individual_pie_delivered as fipd

        INNER JOIN dimension_individual as di
            on di.id=fipd.order_year_id

        INNER JOIN dimension_company as dc
            on dc.id=di.acc_id

        WHERE substring(fipd.order_year, 10, 4) < extract(year from fipd.delivery_time)

		GROUP BY dc.acc_id_number
        ) as QUERY4
		      on QUERY1.acc_id_number = QUERY4.acc_id_number

LEFT JOIN
--QUERY5 Number of deliveries associated with previous rules. (CAKE)
        (SELECT dc.acc_id_number
            ,  count(ficd.id) as Num_Cakes_Delivered

        FROM fact_individual_cake_delivered as ficd

        INNER JOIN dimension_individual as di
            on di.id=ficd.order_year_id

        INNER JOIN dimension_company as dc
            on dc.id=di.acc_id

        WHERE cast(substring(ficd.order_year, 10, 4) as int) < extract(year from ficd.delivery_time)

		GROUP BY dc.acc_id_number
        ) as QUERY5
            on QUERY1.acc_id_number = QUERY5.acc_id_number

LEFT JOIN
--QUERY6 Number of deliveries associated with previous rules. (PIE)
        (SELECT dc.acc_id_number
            ,  count(fipd.id) as Num_Pies_Delivered

        FROM fact_individual_pie_delivered as fipd

        INNER JOIN dimension_individual as di
            on di.id=fipd.order_year_id

        INNER JOIN dimension_company as dc
            on dc.id=di.acc_id

        WHERE substring(fipd.order_year, 10, 4) < extract(year from fipd.delivery_time)

		GROUP BY dc.acc_id_number
        ) as QUERY6
            on QUERY1.acc_id_number = QUERY6.acc_id_number

ORDER BY QUERY1.acc_id_number
		, QUERY2.current_order_year


--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
--THE END
