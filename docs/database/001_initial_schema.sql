-- LetsPay Initial Schema Migration
-- Issue #2: Supabase 데이터베이스 스키마 설정

-- Enable UUID extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- 1. Merchants Table (사업자)
CREATE TABLE merchants (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    auth_user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE,

    email VARCHAR(255) UNIQUE NOT NULL,
    business_name VARCHAR(255) NOT NULL,
    business_number VARCHAR(20) UNIQUE NOT NULL,
    representative_name VARCHAR(100) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    address TEXT,

    bank_code VARCHAR(10),
    bank_account VARCHAR(50),
    bank_holder VARCHAR(100),

    status VARCHAR(20) DEFAULT 'PENDING' CHECK (status IN ('PENDING', 'ACTIVE', 'SUSPENDED')),

    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- 2. Customers Table (고객)
CREATE TABLE customers (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    merchant_id UUID NOT NULL REFERENCES merchants(id) ON DELETE CASCADE,

    name VARCHAR(100) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    email VARCHAR(255),
    memo TEXT,
    tags TEXT[],

    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),

    UNIQUE(merchant_id, phone)
);

-- 3. Bills Table (청구서)
CREATE TABLE bills (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    merchant_id UUID NOT NULL REFERENCES merchants(id) ON DELETE CASCADE,
    customer_id UUID NOT NULL REFERENCES customers(id) ON DELETE CASCADE,
    bill_number VARCHAR(50) UNIQUE NOT NULL,

    amount INTEGER NOT NULL CHECK (amount > 0),
    title VARCHAR(255) NOT NULL,
    description TEXT,
    items JSONB,

    tax_type VARCHAR(20) DEFAULT 'TAX' CHECK (tax_type IN ('TAX', 'TAX_FREE')),
    supply_amount INTEGER,
    tax_amount INTEGER,

    send_type VARCHAR(20) NOT NULL CHECK (send_type IN ('IMMEDIATE', 'SCHEDULED', 'RECURRING')),
    send_channel VARCHAR(20) NOT NULL CHECK (send_channel IN ('ALIMTALK', 'SMS', 'BOTH')),
    scheduled_at TIMESTAMPTZ,
    recurring_rule JSONB,

    status VARCHAR(20) DEFAULT 'DRAFT' CHECK (status IN ('DRAFT', 'PENDING', 'SENT', 'VIEWED', 'PAID', 'CANCELLED', 'EXPIRED')),
    sent_at TIMESTAMPTZ,
    viewed_at TIMESTAMPTZ,
    paid_at TIMESTAMPTZ,
    cancelled_at TIMESTAMPTZ,
    expires_at TIMESTAMPTZ,

    message TEXT,

    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- 4. Payments Table (결제)
CREATE TABLE payments (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    bill_id UUID NOT NULL REFERENCES bills(id) ON DELETE CASCADE,
    merchant_id UUID NOT NULL REFERENCES merchants(id) ON DELETE CASCADE,

    amount INTEGER NOT NULL CHECK (amount > 0),
    method VARCHAR(50),
    pg_provider VARCHAR(50),
    pg_tid VARCHAR(100),

    card_company VARCHAR(50),
    card_number VARCHAR(20),
    installment INTEGER DEFAULT 0,

    status VARCHAR(20) DEFAULT 'PENDING' CHECK (status IN ('PENDING', 'PAID', 'CANCELLED', 'FAILED')),
    paid_at TIMESTAMPTZ,
    cancelled_at TIMESTAMPTZ,
    cancel_reason TEXT,

    settlement_amount INTEGER,
    settlement_at TIMESTAMPTZ,

    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- 5. Cash Receipts Table (현금영수증)
CREATE TABLE cash_receipts (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    payment_id UUID REFERENCES payments(id) ON DELETE SET NULL,
    merchant_id UUID NOT NULL REFERENCES merchants(id) ON DELETE CASCADE,

    type VARCHAR(20) NOT NULL CHECK (type IN ('INCOME', 'EXPENSE')),
    identity_type VARCHAR(20) CHECK (identity_type IN ('PHONE', 'BUSINESS_NUMBER', 'CARD')),
    identity_number VARCHAR(50),
    amount INTEGER NOT NULL CHECK (amount > 0),

    approval_number VARCHAR(50),
    issued_at TIMESTAMPTZ,
    cancelled_at TIMESTAMPTZ,

    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 6. Notification Logs Table (알림 로그)
CREATE TABLE notification_logs (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    bill_id UUID REFERENCES bills(id) ON DELETE CASCADE,
    merchant_id UUID NOT NULL REFERENCES merchants(id) ON DELETE CASCADE,

    channel VARCHAR(20) NOT NULL CHECK (channel IN ('ALIMTALK', 'SMS', 'EMAIL', 'PUSH')),
    recipient VARCHAR(100) NOT NULL,
    status VARCHAR(20) CHECK (status IN ('PENDING', 'SENT', 'DELIVERED', 'FAILED')),

    sent_at TIMESTAMPTZ,
    delivered_at TIMESTAMPTZ,
    error_message TEXT,

    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Indexes for performance
CREATE INDEX idx_merchants_auth_user_id ON merchants(auth_user_id);
CREATE INDEX idx_merchants_status ON merchants(status);

CREATE INDEX idx_customers_merchant_id ON customers(merchant_id);
CREATE INDEX idx_customers_phone ON customers(phone);

CREATE INDEX idx_bills_merchant_id ON bills(merchant_id);
CREATE INDEX idx_bills_customer_id ON bills(customer_id);
CREATE INDEX idx_bills_status ON bills(status);
CREATE INDEX idx_bills_created_at ON bills(created_at DESC);
CREATE INDEX idx_bills_bill_number ON bills(bill_number);

CREATE INDEX idx_payments_merchant_id ON payments(merchant_id);
CREATE INDEX idx_payments_bill_id ON payments(bill_id);
CREATE INDEX idx_payments_status ON payments(status);
CREATE INDEX idx_payments_paid_at ON payments(paid_at DESC);

CREATE INDEX idx_cash_receipts_merchant_id ON cash_receipts(merchant_id);
CREATE INDEX idx_cash_receipts_payment_id ON cash_receipts(payment_id);

CREATE INDEX idx_notification_logs_merchant_id ON notification_logs(merchant_id);
CREATE INDEX idx_notification_logs_bill_id ON notification_logs(bill_id);

-- Updated_at trigger function
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ language 'plpgsql';

-- Apply trigger to tables with updated_at
CREATE TRIGGER update_merchants_updated_at BEFORE UPDATE ON merchants FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
CREATE TRIGGER update_customers_updated_at BEFORE UPDATE ON customers FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
CREATE TRIGGER update_bills_updated_at BEFORE UPDATE ON bills FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
CREATE TRIGGER update_payments_updated_at BEFORE UPDATE ON payments FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
