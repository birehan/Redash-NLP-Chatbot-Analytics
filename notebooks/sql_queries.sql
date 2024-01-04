
            CREATE TABLE IF NOT EXISTS device_type_chart_data (
                "date" TEXT, "device_type" TEXT, "views" INTEGER,
                PRIMARY KEY ("date")
            );
        
            CREATE TABLE IF NOT EXISTS device_type_table_data (
                "device_type" TEXT, "views" INTEGER, "watch_time_hours" DOUBLE PRECISION, "average_view_duration" TEXT,
                PRIMARY KEY ("device_type")
            );
        
            CREATE TABLE IF NOT EXISTS subscription_source_chart_data (
                "date" TEXT, "subscription_source" TEXT, "subscribers" INTEGER,
                PRIMARY KEY ("date")
            );
        
            CREATE TABLE IF NOT EXISTS subscription_source_table_data (
                "subscription_source" TEXT, "subscribers" INTEGER, "subscribers_gained" INTEGER, "subscribers_lost" INTEGER,
                PRIMARY KEY ("subscription_source")
            );
        
            CREATE TABLE IF NOT EXISTS viewership_by_date_table_data (
                "date" TEXT, "views" DOUBLE PRECISION, "watch_time_hours" DOUBLE PRECISION, "average_view_duration" TEXT,
                PRIMARY KEY ("date")
            );
        
            CREATE TABLE IF NOT EXISTS viewer_gender_table_data (
                "viewer_gender" TEXT, "views_%" DOUBLE PRECISION, "average_view_duration" TEXT, "average_percentage_viewed_%" DOUBLE PRECISION, "watch_time_hours_%" DOUBLE PRECISION,
                PRIMARY KEY ("viewer_gender")
            );
        
            CREATE TABLE IF NOT EXISTS traffic_source_chart_data (
                "date" TEXT, "traffic_source" TEXT, "views" INTEGER,
                PRIMARY KEY ("date")
            );
        
            CREATE TABLE IF NOT EXISTS traffic_source_table_data (
                "traffic_source" TEXT, "views" DOUBLE PRECISION, "watch_time_hours" DOUBLE PRECISION, "average_view_duration" TEXT, "impressions" DOUBLE PRECISION, "impressions_click-through_rate_%" DOUBLE PRECISION,
                PRIMARY KEY ("traffic_source")
            );
        
            CREATE TABLE IF NOT EXISTS subtitles_and_cc_chart_data (
                "date" TEXT, "subtitles_and_cc" TEXT, "views" INTEGER,
                PRIMARY KEY ("date")
            );
        
            CREATE TABLE IF NOT EXISTS subtitles_and_cc_table_data (
                "subtitles_and_cc" TEXT, "views" INTEGER, "watch_time_hours" DOUBLE PRECISION, "average_view_duration" TEXT,
                PRIMARY KEY ("subtitles_and_cc")
            );
        
            CREATE TABLE IF NOT EXISTS new_and_returning_viewers_chart_data (
                "date" TEXT, "new_and_returning_viewers" TEXT, "views" INTEGER,
                PRIMARY KEY ("date")
            );
        
            CREATE TABLE IF NOT EXISTS new_and_returning_viewers_table_data (
                "new_and_returning_viewers" TEXT, "views" INTEGER, "watch_time_hours" DOUBLE PRECISION, "average_view_duration" TEXT,
                PRIMARY KEY ("new_and_returning_viewers")
            );
        
            CREATE TABLE IF NOT EXISTS operating_system_chart_data (
                "date" TEXT, "operating_system" TEXT, "views" INTEGER,
                PRIMARY KEY ("date")
            );
        
            CREATE TABLE IF NOT EXISTS operating_system_table_data (
                "operating_system" TEXT, "views" INTEGER, "watch_time_hours" DOUBLE PRECISION, "average_view_duration" TEXT,
                PRIMARY KEY ("operating_system")
            );
        
            CREATE TABLE IF NOT EXISTS cities_chart_data (
                "date" TEXT, "cities" TEXT, "city_name" TEXT, "views" INTEGER,
                PRIMARY KEY ("date")
            );
        
            CREATE TABLE IF NOT EXISTS cities_table_data (
                "cities" TEXT, "city_name" TEXT, "geography" TEXT, "geography.1" TEXT, "views" INTEGER, "watch_time_hours" DOUBLE PRECISION, "average_view_duration" TEXT,
                PRIMARY KEY ("cities")
            );
        
            CREATE TABLE IF NOT EXISTS viewer_age_table_data (
                "viewer_age" TEXT, "views_%" DOUBLE PRECISION, "average_view_duration" TEXT, "average_percentage_viewed_%" DOUBLE PRECISION, "watch_time_hours_%" DOUBLE PRECISION,
                PRIMARY KEY ("viewer_age")
            );
        
            CREATE TABLE IF NOT EXISTS subscription_status_chart_data (
                "date" TEXT, "subscription_status" TEXT, "views" INTEGER,
                PRIMARY KEY ("date")
            );
        
            CREATE TABLE IF NOT EXISTS subscription_status_table_data (
                "subscription_status" TEXT, "views" INTEGER, "watch_time_hours" DOUBLE PRECISION, "average_view_duration" TEXT,
                PRIMARY KEY ("subscription_status")
            );
        
            CREATE TABLE IF NOT EXISTS geography_chart_data (
                "date" TEXT, "geography" TEXT, "views" INTEGER,
                PRIMARY KEY ("date")
            );
        
            CREATE TABLE IF NOT EXISTS geography_table_data (
                "geography" TEXT, "views" INTEGER, "watch_time_hours" DOUBLE PRECISION, "average_view_duration" TEXT,
                PRIMARY KEY ("geography")
            );
        
            CREATE TABLE IF NOT EXISTS sharing_service_chart_data (
                "date" TEXT, "sharing_service" TEXT, "shares" INTEGER,
                PRIMARY KEY ("date")
            );
        
            CREATE TABLE IF NOT EXISTS sharing_service_table_data (
                "sharing_service" TEXT, "shares" INTEGER,
                PRIMARY KEY ("sharing_service")
            );
        
            CREATE TABLE IF NOT EXISTS content_type_chart_data (
                "date" TEXT, "content_type" TEXT, "views" INTEGER,
                PRIMARY KEY ("date")
            );
        
            CREATE TABLE IF NOT EXISTS content_type_table_data (
                "content_type" TEXT, "views" INTEGER, "watch_time_hours" DOUBLE PRECISION, "average_view_duration" TEXT,
                PRIMARY KEY ("content_type")
            );
        
            CREATE TABLE IF NOT EXISTS totals_table_data (
                "date" TEXT, "views" DOUBLE PRECISION, "subscribers" DOUBLE PRECISION, "shares" DOUBLE PRECISION,
                PRIMARY KEY ("date")
            );
        