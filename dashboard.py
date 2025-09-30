import datetime

import numpy as np
import pandas as pd
import streamlit as st
import altair as alt


st.set_page_config(page_title="Dashboard with flex layout", layout="wide")
np.random.seed(42)


with st.container(horizontal=True, vertical_alignment="bottom"):
    st.header("Dashboard with flex layout", width="stretch")

    st.selectbox(
        "Filter by", ["Product Line", "Metrics", "Reports", "Department", "Region", "Category"], width=150
    )
    st.selectbox(
        "Search for KPIs",
        ["Revenue Growth", "Customer Retention", "Product Quality"],
        width=200
    )
    st.selectbox(
        "Search for Metrics",
        [
            "All Metrics for KPI",
            "Monthly Revenue",
            "Quarterly Growth",
        ],
        width=200
    )

view = st.segmented_control(
    "View",
    ["Performance Overview", "Product Metrics", "Market Trends"],
    default="Performance Overview",
    label_visibility="collapsed"
)

if view == "Performance Overview":
    
    # TODO: On mobile this page looks a bit broken. 
    
    # Add top row metrics with deltas
    with st.container(horizontal=True):
        st.metric("Total Revenue", "$5.8M", delta="+12.4%", width="stretch", border=True)
        st.metric("Active Products", "42", delta="+5", width="stretch", border=True)
        st.metric("Customer Satisfaction", "8.7/10", delta="+0.3", width="stretch", border=True)
        st.metric("YTD Growth", "18.2%", delta="+3.5%", width="stretch", border=True)
    
    col1, col2 = st.columns([2, 1])
    # TODO: height="stretch" is not working. 
    with col1.container(border=True, height="stretch"):
        
        st.markdown("""
        This dashboard provides a comprehensive overview of our product performance metrics across North America. The Smart Devices product line, specifically IoT Sensors, has shown consistent growth over the past quarter with a 12.4% increase in total revenue.
        
        Key indicators suggest that our enterprise market strategy is working effectively. Customer satisfaction scores have improved, and our active product count continues to expand. The monthly reporting cycle allows us to track these metrics closely and make data-driven adjustments to our strategy.
        """)

        
        # TODO: Need grid layout here. 
        # TODO: Would be nice to set a bigger vertical gap once this wraps.
        with st.container(horizontal=True):
            
            def show_element(text, badge_text, icon, color="blue"):
                with st.container(gap=None, width=160): 
                    st.write(f"**{text}**")
                    st.badge(badge_text, icon=icon, color=color)

            show_element("REGION", "North America", ":material/globe:", color="green")
            show_element("PRODUCT LINE", "Smart Devices", ":material/label:")
            show_element("PRODUCT CATEGORY", "IoT Sensors", ":material/label:")
            show_element("PRODUCT MANAGER", "Thompson, R&D-5", ":material/person:", color="violet")
            show_element("MARKET ANALYST", "Chen, MKT-3", ":material/person:", color="violet")
            show_element("DATA ANALYST", "Rivera, DATA-1", ":material/person:", color="violet")
            show_element("REPORTING CYCLE", "Monthly", ":material/cycle:", color="orange")
            show_element("SYSTEMS", "CRM", ":material/label:")
            show_element("TARGET MARKET", "Enterprise", ":material/label:")
            show_element("KEY REPORTS", "Sales Analysis", ":material/label:")
            show_element("DATA SOURCE", "Central Database", ":material/label:")
            show_element("TRACKING METHOD", "Automated", ":material/label:")
        
        
           
            
    with col2:
        with st.container(border=True, height="stretch"):
            st.write(":small[Performance Score]")
            
            # Bar chart with multiple categories
            score_data = pd.DataFrame({
                "Category": ["A", "B", "C", "D"],
                "Score": [72, 85, 65, 70]
            })
            
            st.bar_chart(
                score_data,
                x="Category",
                y="Score",
                height=150,
                use_container_width=True
            )
            
        with st.container(border=True, height="stretch"):
            st.write(":small[Monthly Performance Trend]")
            
            # Create more comprehensive data for line chart with multiple metrics
            months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
            
            trend_data = pd.DataFrame({
                "Overall Score": [58, 60, 62, 65, 68, 72],
                "Revenue": [55, 58, 64, 67, 72, 78],
                "Customer Satisfaction": [65, 63, 60, 62, 65, 68]
            }, index=months)
            
            # Display simple line chart with multiple lines
            st.line_chart(
                trend_data,
                height=150,
                use_container_width=True
            )

    with st.container(border=True):
        st.write(":small[Performance Controls]")
        # Create sample data for the table
        stability_data = pd.DataFrame({
            "KPI Code": ["KPI-001", "KPI-002", "KPI-003", "KPI-004", "KPI-005", "KPI-006", "KPI-007", "KPI-008", "KPI-009", "KPI-010", "KPI-011", "KPI-012", "KPI-013", "KPI-014", "KPI-015", "KPI-016", "KPI-017", "KPI-018", "KPI-019", "KPI-020"],
            "Performance Indicator": [
                "Revenue Growth Rate",
                "Customer Acquisition Cost",
                "Customer Lifetime Value",
                "Churn Rate",
                "Net Promoter Score",
                "Gross Margin",
                "Operating Expense Ratio",
                "Inventory Turnover",
                "Days Sales Outstanding",
                "Return on Investment",
                "Market Share",
                "Product Defect Rate",
                "Employee Satisfaction",
                "Website Conversion Rate",
                "Average Order Value",
                "Sales Cycle Length",
                "Lead-to-Customer Ratio",
                "Customer Support Resolution Time",
                "Social Media Engagement",
                "Supply Chain Efficiency"
            ],
            "Target Value": [
                "15%", "80$", "450$", "5%", "45", "35%", "25%", "12", "30", "22%", 
                "18%", "0.5%", "4.2/5", "3.5%", "120$", "14 days", "25%", "4h", "8%", "92%"
            ],
            "Status": [
                "On Track", "At Risk", "On Track", "On Track", "Below Target", 
                "On Track", "At Risk", "On Track", "Below Target", "On Track",
                "On Track", "At Risk", "On Track", "On Track", "Below Target",
                "On Track", "On Track", "At Risk", "On Track", "On Track"
            ],
            "Department": [
                "Sales", "Marketing", "Sales", "Customer Success", "Customer Success",
                "Finance", "Finance", "Operations", "Finance", "Executive",
                "Marketing", "Production", "HR", "Marketing", "Sales",
                "Sales", "Marketing", "Support", "Marketing", "Operations"
            ],
            "Review Frequency": [
                "Monthly", "Quarterly", "Quarterly", "Monthly", "Quarterly",
                "Monthly", "Monthly", "Weekly", "Monthly", "Quarterly",
                "Quarterly", "Daily", "Quarterly", "Weekly", "Monthly",
                "Monthly", "Monthly", "Daily", "Weekly", "Monthly"
            ],
        })
        
        # Display the dataframe
        st.dataframe(
            stability_data,
            hide_index=True,
            use_container_width=True,
            column_config={
                "Metric ID": st.column_config.TextColumn("Metric ID"),
                "Metric Name": st.column_config.TextColumn("Metric Name"),
                "Control ID": st.column_config.TextColumn("Control ID"),
                "Control Name": st.column_config.TextColumn("Control Name"),
                "Performance Dimension": st.column_config.TextColumn("Performance Dimension"),
                "Critical Product Element": st.column_config.TextColumn("Critical Product Element")
            }
        )

elif view == "Product Metrics":

    col1, col2, col3, col4 = st.columns([1, 1, 1, 2], border=True)
    col1.metric("Total number of products", 5427, delta="+124")
    col2.metric("Underperforming products", 18, delta="-3")
    col3.metric("Overperforming products", 36, delta="+8")

    data = pd.DataFrame(
        {
            "Category": ["Values"],
            "Low performance": [12],
            "Meeting targets": [78],
            "Needs review": [10],
        }
    )
    with col4:
        with st.container(gap=None):
            # TODO: Would be even nicer if we had `label` on the chart.
            st.write(":small[Total number of products and proportion of underperforming items]")
            
            chart = alt.Chart(data).transform_fold(
                ['Low performance', 'Needs review', 'Meeting targets'],
                as_=['Metric', 'Value']
            ).transform_joinaggregate(
                total='sum(Value)',
                groupby=['Category']
            ).transform_window(
                sort=[alt.SortField('Value', order='descending')],
                sort_metric_index='rank()'
            ).mark_bar().encode(
                x=alt.X('Value:Q', stack='normalize', axis=None),
                y=alt.Y('Category:N', axis=None),
                color=alt.Color('Metric:N', scale=alt.Scale(
                    domain=['Meeting targets', 'Low performance', 'Needs review'],
                ), sort=alt.EncodingSortField(field='Value', order='descending'), title=None),
                order=alt.Order('sort_metric_index:Q'),
                tooltip=['Metric:N', 'Value:Q']
            ).properties(
                height=70,
                padding={'top': 8, 'bottom': 0, 'left': 0, 'right': 0}
            ).configure_view(
                strokeWidth=0
            ).configure_legend(
                orient='bottom',
                padding=10,
                offset=0
            )
            st.altair_chart(chart, use_container_width=True)

    with st.container(border=True):
        with st.container(horizontal=True, vertical_alignment="center"):
            st.markdown(":small[Underperforming products over time]", width="stretch")
            st.markdown(":small[Period]", width="content")
            st.date_input(
                "Period", value=(datetime.date(2023, 6, 1), datetime.date(2024, 6, 1)), width=200, format="DD.MM.YYYY", label_visibility="collapsed"
            )
            st.markdown(":small[Show selected period by]", width="content")
            st.selectbox("Show selected period by", ["Year", "Quarter", "Month"], width=150, label_visibility="collapsed")

        # Generate sample data
        dates = pd.date_range(start="2023-06-01", end="2024-06-01", freq="D")
        df = pd.DataFrame(
            {
                "Smart Home": np.random.randint(0, 20, size=10),
                "Office IoT": np.random.randint(0, 20, size=10),
                "Industrial Sensors": np.random.randint(0, 20, size=10),
            },
            index=pd.date_range(start="2023-06-01", end="2024-06-01", periods=10),
        )
        # TODO: Would be great to set our color names here. Or alternatively define them
        # in advanced theming.
        st.line_chart(df, height=300)


    with st.container(border=True):
        st.write(":small[Performance score over time]")

        # Generate sample data
        dates = pd.date_range(start="2023-06-01", end="2024-06-01", freq="D")
        df = pd.DataFrame(
            {
                "Company Average": np.random.randint(0, 20, size=10),
                "Product Line": np.random.randint(0, 20, size=10),
            },
            index=pd.date_range(start="2023-06-01", end="2024-06-01", periods=10),
        )
        st.line_chart(df, height=300)

elif view == "Market Trends":
    
    # Header metrics in columns
    col1, col2, col3, col4 = st.columns([1, 1, 1, 2], border=True)
    col1.metric("Market Size", "$4.3B", delta="+8.2%")
    col2.metric("Market Share", "23.5%", delta="+2.1%")
    col3.metric("Competitors", "14", delta="-2")

    data = pd.DataFrame(
        {
            "Category": ["Values"],
            "Our Company": [23.5],
            "Main Competitor": [18.2],
            "Others": [58.3],
        }
    )
    with col4:
        with st.container(gap=None):
            st.write(":small[Market share distribution]")
            
            chart = alt.Chart(data).transform_fold(
                ['Our Company', 'Main Competitor', 'Others'],
                as_=['Segment', 'Value']
            ).transform_joinaggregate(
                total='sum(Value)',
                groupby=['Category']
            ).transform_window(
                sort=[alt.SortField('Value', order='descending')],
                sort_metric_index='rank()'
            ).mark_bar().encode(
                x=alt.X('Value:Q', stack='normalize', axis=None),
                y=alt.Y('Category:N', axis=None),
                color=alt.Color('Segment:N', scale=alt.Scale(
                    domain=['Our Company', 'Main Competitor', 'Others'],
                ), sort=alt.EncodingSortField(field='Value', order='descending'), title=None),
                order=alt.Order('sort_metric_index:Q'),
                tooltip=['Segment:N', 'Value:Q']
            ).properties(
                height=70,
                padding={'top': 8, 'bottom': 0, 'left': 0, 'right': 0}
            ).configure_view(
                strokeWidth=0
            ).configure_legend(
                orient='bottom',
                padding=10,
                offset=0
            )
            st.altair_chart(chart, use_container_width=True)

    # Top half of page has two columns
    col1, col2 = st.columns([3, 2], border=True)
    
    # Market trends over time
    with col1:
        with st.container(horizontal=True, vertical_alignment="center"):
            st.markdown(":small[Market Share Trends]", width="stretch")
            st.markdown(":small[Time Period]", width="content")
            st.date_input(
                "Period", value=(datetime.date(2023, 1, 1), datetime.date(2024, 6, 1)), 
                width=200, format="DD.MM.YYYY", label_visibility="collapsed"
            )
            st.markdown(":small[View by]", width="content")
            st.selectbox("View by", ["Quarter", "Month", "Year"], width=150, label_visibility="collapsed")

        # Create market share trend data
        quarters = ["Q1 2023", "Q2 2023", "Q3 2023", "Q4 2023", "Q1 2024", "Q2 2024"]
        trend_data = pd.DataFrame({
            "Our Company": [18.2, 19.5, 20.3, 21.8, 22.6, 23.5],
            "Competitor A": [21.5, 20.8, 19.2, 18.8, 18.5, 18.2],
            "Competitor B": [15.3, 14.8, 14.5, 14.0, 13.8, 13.6],
            "Competitor C": [12.2, 12.5, 13.0, 13.2, 13.0, 12.8],
            "Others": [32.8, 32.4, 33.0, 32.2, 32.1, 31.9]
        }, index=quarters)
        
        st.line_chart(trend_data, height=300)
        
    # Market analysis and insights
    with col2:
        st.write(":small[Competitive Analysis]")
                
        # Bar chart comparing key metrics against competitors
        metrics = ["Price", "Quality", "Innovation", "Brand Value"]
        companies = ["Our Company", "Competitor A", "Competitor B"]
        
        # Reshape data for grouped bar chart
        market_data = []
        for metric in metrics:
            for company in companies:
                if company == "Our Company":
                    score = np.random.randint(70, 90)
                elif company == "Competitor A":
                    score = np.random.randint(65, 85)
                else:
                    score = np.random.randint(60, 80)
                market_data.append({"Metric": metric, "Company": company, "Score": score})
        
        market_df = pd.DataFrame(market_data)
        
        # Group by Metric and pivot
        pivot_df = market_df.pivot(index="Metric", columns="Company", values="Score")
        
        # Plot bar chart
        st.bar_chart(pivot_df, height=270)
    
    # Bottom section for regional market data
    with st.container(border=True):
        st.write(":small[Regional Market Analysis]")
        
        # Create sample data for regions
        region_data = pd.DataFrame({
            "Region": ["North America", "Europe", "Asia Pacific", "Latin America", "Middle East & Africa"],
            "Market Size ($M)": [1850, 1200, 850, 250, 150],
            "Growth Rate (%)": [7.2, 5.8, 12.5, 9.3, 6.7],
            "Our Market Share (%)": [28.5, 22.0, 18.5, 15.0, 10.5],
            "Competitors": [6, 8, 10, 5, 3],
            "CAGR (3yr)": ["8.2%", "6.5%", "13.2%", "10.1%", "7.5%"],
            "Market Trend": ["Growing", "Stable", "Rapidly Growing", "Growing", "Stable"]
        })
        
        # Display the dataframe
        st.dataframe(
            region_data,
            hide_index=True,
            use_container_width=True,
            column_config={
                "Region": st.column_config.TextColumn("Region", width="medium"),
                "Market Size ($M)": st.column_config.NumberColumn("Market Size ($M)", format="$%d M"),
                "Growth Rate (%)": st.column_config.NumberColumn("Growth Rate (%)", format="%.1f%%"),
                "Our Market Share (%)": st.column_config.NumberColumn("Our Market Share (%)", format="%.1f%%"),
                "Competitors": st.column_config.NumberColumn("Competitors"),
                "CAGR (3yr)": st.column_config.TextColumn("CAGR (3yr)"),
                "Market Trend": st.column_config.TextColumn("Market Trend")
            }
        )