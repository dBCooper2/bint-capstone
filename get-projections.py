import pandas as pd

def calculate_projections(investment, revenue_estimates, margin_range, expense_ratio):
    results = []
    
    for revenue in revenue_estimates:
        for margin in margin_range:
            gross_profit = revenue * margin
            net_profit = gross_profit * (1 - expense_ratio)
            payback_period = investment / net_profit if net_profit > 0 else None
            
            results.append({
                "Revenue": revenue,
                "Margin": margin,
                "Gross Profit": gross_profit,
                "Net Profit": net_profit,
                "Payback Period (Years)": payback_period,
            })
    
    return pd.DataFrame(results)

# Assumptions
investment_range = [2800000, 6870000]  # Min and max investment
revenue_estimates = [2000000, 3430013, 4500000]  # Conservative, median, optimistic
margin_range = [0.10, 0.12, 0.15]  # Gross profit margin estimates
expense_ratio = 0.40  # 40% of gross profit goes to operating expenses

# Create an Excel writer
with pd.ExcelWriter("culvers_profitability.xlsx", engine="openpyxl") as writer:
    for investment in investment_range:
        df = calculate_projections(investment, revenue_estimates, margin_range, expense_ratio)
        sheet_name = f"Investment_{investment//1000000}M"
        df.to_excel(writer, sheet_name=sheet_name, index=False)

print("Excel file generated: culvers_profitability.xlsx")
