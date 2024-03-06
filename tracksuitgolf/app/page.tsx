import { createClient } from '@/utils/supabase/server';

export default async function Notes() {
  const supabase = createClient();
  const { data: players } = await supabase.from("player").select();

  return <pre>{JSON.stringify(players, null, 2)}</pre>
}
