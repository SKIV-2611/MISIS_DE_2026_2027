import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv('sales.csv')
    print('First 5 rows:')
    print(df.head())
    print('\nCSV info:')
    df.info()
    print('\nNan statistics:')
    print(df.isna().sum())
    print('\nNumeric columns statistics:')
    print(df.describe())

    # Find sales over 10000
    df_over_10_000 = df[df['sales'] > 10000]
    print('\nSales over 10_000:')
    print(df_over_10_000)
    df_over_10_000.to_csv('sales_over_10000.csv', index=False, sep=',')

    # Find sales in March
    print('\nMarch 2023 sales:')
    df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
    end_of_feb = pd.to_datetime('2023-02-28', format='%Y-%m-%d')
    start_of_apr = pd.to_datetime('2023-04-01', format='%Y-%m-%d')
    df_march = df[(df['date'] > end_of_feb) & (df['date'] < start_of_apr)]\
        .reset_index(drop=True)
    print(df_march)
    df_march.to_csv('sales_in_march.csv', index=False, sep=',')

    # Filter with several conditions
    df_sev_filtered = df[(df['sales'] < 24000) | (df['city'] == 'СПб') & (~(df['category'] == 'Продукты'))]
    print('\nSeveral filters applied:')
    print(df_sev_filtered)
    df_sev_filtered.to_csv('sales_several_filters.csv', index=False, sep=',')

    # Group sales by city
    df_cities = df.groupby(by='city')['sales'].sum().sort_values(ascending=False)
    print('\nTotal sales by city:')
    print(df_cities)
    df_cities.to_csv('sales_by_city.csv', sep=',')

    # Average cost
    df['cost'] = df['quantity'] * df['price']
    df_average = df.groupby(by='category')['cost'].mean().sort_values(ascending=False).round(3)
    print('\nAverage cost by category')
    print(df_average)
    df_average.to_csv('average_cost.csv')

    # Top 5 by sales
    df_top_5 = df.groupby(by='product_id')['sales'].sum().sort_values(ascending=False).head(5)
    print('\nTop 5 product_id by sales:')
    print(df_top_5)
    df_top_5.to_csv('sales_top_5.csv')

    # No NaNs, but if they were
    # Fill NaN with mean values
    df[['sales',
        'quantity',
        'price']] = df[['sales',
                        'quantity',
                        'price']].fillna(df[['sales', 'quantity', 'price']].mean())
    # Both for non-numeric columns, such as "city",
    # and for "product_id" replacing NaN with mean value makes no sense at all

    # Drop rows with NaN
    df.dropna(inplace=True)

    # Create new columns based on existing
    df['month'] = df['date'].dt.month
    df['month_name'] = df['date'].dt.month_name()

    print('\nCleaned sales head and tail + month/month_name columns:')

    print(df.head())
    print(df.tail())
    df.to_csv('cleaned_added_sales.csv', index=False)



