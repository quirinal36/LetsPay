-- LetsPay Auth Trigger
-- Issue #3: Auto-create merchant on signup

-- Create trigger to auto-create merchant record when user signs up
CREATE OR REPLACE FUNCTION public.handle_new_user()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO public.merchants (
        auth_user_id,
        email,
        business_name,
        business_number,
        representative_name,
        phone,
        status
    )
    VALUES (
        NEW.id,
        NEW.email,
        '',
        '',
        '',
        '',
        'PENDING'
    );
    RETURN NEW;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

-- Drop existing trigger if exists
DROP TRIGGER IF EXISTS on_auth_user_created ON auth.users;

-- Create trigger on auth.users table
CREATE TRIGGER on_auth_user_created
    AFTER INSERT ON auth.users
    FOR EACH ROW EXECUTE FUNCTION public.handle_new_user();
