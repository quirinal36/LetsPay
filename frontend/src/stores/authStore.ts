import { create } from 'zustand'
import { persist } from 'zustand/middleware'
import type { User, Session } from '@supabase/supabase-js'
import { supabase, signIn, signUp, signOut, signInWithGoogle } from '@/lib/supabase'

interface AuthState {
  user: User | null
  session: Session | null
  isLoading: boolean
  error: string | null
  initialize: () => Promise<void>
  login: (email: string, password: string) => Promise<void>
  register: (email: string, password: string) => Promise<void>
  registerWithBusinessInfo: (
    email: string,
    password: string,
    phone: string,
    businessName: string
  ) => Promise<boolean>
  loginWithGoogle: () => Promise<void>
  logout: () => Promise<void>
  clearError: () => void
}

export const useAuthStore = create<AuthState>()(
  persist(
    (set) => ({
      user: null,
      session: null,
      isLoading: true,
      error: null,

      initialize: async () => {
        try {
          const { data } = await supabase.auth.getSession()
          set({
            session: data.session,
            user: data.session?.user ?? null,
            isLoading: false,
          })
          supabase.auth.onAuthStateChange((_event, session) => {
            set({ session, user: session?.user ?? null })
          })
        } catch {
          set({ isLoading: false, error: 'Failed to initialize auth' })
        }
      },

      login: async (email, password) => {
        set({ isLoading: true, error: null })
        const { data, error } = await signIn(email, password)
        if (error) {
          set({ isLoading: false, error: error.message })
        } else {
          set({ session: data.session, user: data.user, isLoading: false })
        }
      },

      register: async (email, password) => {
        set({ isLoading: true, error: null })
        const { data, error } = await signUp(email, password)
        if (error) {
          set({ isLoading: false, error: error.message })
        } else {
          set({ session: data.session, user: data.user, isLoading: false })
        }
      },

      registerWithBusinessInfo: async (email, password, phone, businessName) => {
        set({ isLoading: true, error: null })
        const { data, error } = await signUp(email, password)
        if (error) {
          set({ isLoading: false, error: error.message })
          return false
        }

        // Save business info to backend
        try {
          const response = await fetch(`${import.meta.env.VITE_API_URL}/auth/signup`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
              email,
              phone,
              business_name: businessName,
              supabase_user_id: data.user?.id,
            }),
          })
          if (!response.ok) {
            const errorData = await response.json().catch(() => ({}))
            const errorMessage = errorData.detail || '사업자 정보 저장에 실패했습니다'
            set({ isLoading: false, error: errorMessage })
            return false
          }
        } catch (err) {
          console.error('Failed to save business info:', err)
          set({ isLoading: false, error: '서버 연결에 실패했습니다. 잠시 후 다시 시도해주세요.' })
          return false
        }

        set({ session: data.session, user: data.user, isLoading: false })
        return true
      },

      loginWithGoogle: async () => {
        set({ isLoading: true, error: null })
        const { error } = await signInWithGoogle()
        if (error) {
          set({ isLoading: false, error: error.message })
        }
      },

      logout: async () => {
        set({ isLoading: true })
        await signOut()
        set({ user: null, session: null, isLoading: false })
      },

      clearError: () => set({ error: null }),
    }),
    { name: 'auth-storage', partialize: (state) => ({ user: state.user }) }
  )
)
