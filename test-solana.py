from solana_fcg_tool import SolanaAnalyzer
analyzer = SolanaAnalyzer('test/onre-sol')
result = analyzer.find_symbols('take_offer_two')
if result:
    print(result)
else:
    print("wrong")