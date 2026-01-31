-- LetsPay Row Level Security Policies
-- Issue #2: RLS for data isolation

-- Enable RLS on all tables
ALTER TABLE merchants ENABLE ROW LEVEL SECURITY;
ALTER TABLE customers ENABLE ROW LEVEL SECURITY;
ALTER TABLE bills ENABLE ROW LEVEL SECURITY;
ALTER TABLE payments ENABLE ROW LEVEL SECURITY;
ALTER TABLE cash_receipts ENABLE ROW LEVEL SECURITY;
ALTER TABLE notification_logs ENABLE ROW LEVEL SECURITY;

-- Helper function: Get current merchant_id from auth
CREATE OR REPLACE FUNCTION get_current_merchant_id()
RETURNS UUID AS $$
BEGIN
    RETURN (
        SELECT id FROM merchants
        WHERE auth_user_id = auth.uid()
        LIMIT 1
    );
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

-- MERCHANTS: Users can only see/edit their own merchant record
CREATE POLICY "Users can view own merchant" ON merchants
    FOR SELECT USING (auth_user_id = auth.uid());

CREATE POLICY "Users can update own merchant" ON merchants
    FOR UPDATE USING (auth_user_id = auth.uid());

CREATE POLICY "Users can insert merchant on signup" ON merchants
    FOR INSERT WITH CHECK (auth_user_id = auth.uid());

-- CUSTOMERS: Merchants can only access their own customers
CREATE POLICY "Merchants can view own customers" ON customers
    FOR SELECT USING (merchant_id = get_current_merchant_id());

CREATE POLICY "Merchants can insert own customers" ON customers
    FOR INSERT WITH CHECK (merchant_id = get_current_merchant_id());

CREATE POLICY "Merchants can update own customers" ON customers
    FOR UPDATE USING (merchant_id = get_current_merchant_id());

CREATE POLICY "Merchants can delete own customers" ON customers
    FOR DELETE USING (merchant_id = get_current_merchant_id());

-- BILLS: Merchants can only access their own bills
CREATE POLICY "Merchants can view own bills" ON bills
    FOR SELECT USING (merchant_id = get_current_merchant_id());

CREATE POLICY "Merchants can insert own bills" ON bills
    FOR INSERT WITH CHECK (merchant_id = get_current_merchant_id());

CREATE POLICY "Merchants can update own bills" ON bills
    FOR UPDATE USING (merchant_id = get_current_merchant_id());

CREATE POLICY "Merchants can delete own bills" ON bills
    FOR DELETE USING (merchant_id = get_current_merchant_id());

-- PAYMENTS: Merchants can only access their own payments
CREATE POLICY "Merchants can view own payments" ON payments
    FOR SELECT USING (merchant_id = get_current_merchant_id());

CREATE POLICY "System can insert payments" ON payments
    FOR INSERT WITH CHECK (true);

-- CASH_RECEIPTS: Merchants can only access their own
CREATE POLICY "Merchants can view own cash_receipts" ON cash_receipts
    FOR SELECT USING (merchant_id = get_current_merchant_id());

CREATE POLICY "Merchants can insert own cash_receipts" ON cash_receipts
    FOR INSERT WITH CHECK (merchant_id = get_current_merchant_id());

-- NOTIFICATION_LOGS: Merchants can only access their own
CREATE POLICY "Merchants can view own notification_logs" ON notification_logs
    FOR SELECT USING (merchant_id = get_current_merchant_id());

-- Grant access to authenticated users
GRANT USAGE ON SCHEMA public TO authenticated;
GRANT ALL ON ALL TABLES IN SCHEMA public TO authenticated;
GRANT ALL ON ALL SEQUENCES IN SCHEMA public TO authenticated;
